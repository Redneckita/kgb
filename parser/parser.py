import os
import re
import time
import datetime
from kgb import settings as settings
from quake3 import rcon
from database import api
from random import choice

class Parser:

    def __init__(self, log_file):

        self.full_file_name = log_file
        self.file_dimension = os.path.getsize(self.full_file_name)
        self.text_to_process = []

    def read(self):

        if os.path.getsize(self.full_file_name) > self.file_dimension:
            logfile = open(self.full_file_name, "r")
            logfile.seek(self.file_dimension)
            self.text_to_process = logfile.read()
            logfile.close()
            self.file_dimension = os.path.getsize(self.full_file_name)
            self.text_to_process = self.text_to_process.split('\n')
            return self.text_to_process
        elif os.path.getsize(self.full_file_name) < self.file_dimension:
            self.file_dimension = os.path.getsize(self.full_file_name)
            return None

class Evaluator:

    def __init__(self, host_address, host_port, rcon_passwd, api_url , api_user, api_key):
        self.host_address = host_address
        self.host_port = host_port
        self.rcon_passwd = rcon_passwd
        self.rc = rcon.Rcon(self.host_address, self.host_port, self.rcon_passwd, api_url, api_user, api_key)

        self.api_url = api_url
        self.api_user = api_user
        self.api_key = api_key
        self.api = api.Api(api_user, api_key, api_url)

    def evaluate_config(self):
        server_config_found, server_config_objs = self.api.get_server_configs()
        if server_config_found:
            for item in server_config_objs:
                if item['code'] == 'SPAM_MESSAGE':
                    settings.SPAM_MESSAGES.append(item['value'])
                elif item['code'] == 'SPAM_MESSAGES_TIMEOUT':
                    settings.SPAM_MESSAGES_TIMEOUT = item['value']
                elif item['code'] == 'SERVER_CLOSED':
                    settings.SERVER_CLOSED = item['value']
                elif item['code'] == 'SERVER_CLOSED_TIMEOUT':
                    settings.SERVER_CLOSED_TIMEOUT = item['value']

    def put_spam(self):
        self.rc.putMessage(None, str(choice(settings.SPAM_MESSAGES))) 

    def start(self):
        self.rc.putMessage(None, settings.BOT_MESSAGE_START)            

    def evaluate_player(self, data):            

        res = None
        if data.find("ClientUserinfo:") != -1:
            res = re.search(r"ClientUserinfo: (?P<id>\d+).*\\ip\\(?P<ip>\d*\.\d*\.\d*\.\d*).*\\name\\(?P<name>.*?)(\\|$)",data)
        elif data.find("ClientUserinfoChanged:")!=-1:
            res = re.search(r"ClientUserinfoChanged: (?P<id>\d+).*n\\(?P<name>.*?)\\t", data)

        if res:
            player = self.rc.getPlayer(res.group("id"))
            if player and player.guid.strip() != '':
                player_found, player_obj = self.api.get_player(player.guid)
                if not player_found:
                    # 'player non trovato, lo inserisco'
                    player_found, player_obj = self.api.insert_player(player)    
                    if player_found:
                        # 'player inserito'
                        pass
                    else:
                        # 'errore: player non inserito'
                        pass
                
                if player_found:

                    # 'player esiste, verifico se inserire alias'
                    alias_found, alias_obj = self.api.get_alias(player.guid, player.name)
                    if alias_found is not None and not alias_found:
                        # 'alias non trovato, lo inserisco'
                        alias_found, alias_obj = self.api.insert_alias(player, player_obj['resource_uri'])
                        if alias_found:
                            # 'alias inserito'
                            pass
                    else:
                        # 'alias esiste'
                        pass


                    # 'player esiste, verifico se inserire profile'
                    profile_found, profile_obj = self.api.get_profile(player.guid, player.address.split(":")[0])
                    if profile_found is not None and not profile_found:
                        # 'profile non trovato, lo inserisco'
                        profile_found, profile_obj = self.api.insert_profile(player, player_obj['resource_uri'])
                        if profile_found:
                            # 'profile inserito'
                            pass
                    else:
                        # 'profile esiste'
                        pass


        if data.find("ClientBegin:") !=  -1:                                                           # *** CLIENTCONNECT
            res = re.search(r"ClientBegin: (?P<id>\d+)", data)
            if res:
                player = self.rc.getPlayer(res.group("id"))
                
                if player:
                    # 'player esiste, verifico se e' bannato
                    bans_found, bans_obj = self.api.get_bans(player.guid)
                    if bans_found is not None and bans_found:
                        # 'verifico se esiste un ban attivo'
                        for ban in bans_obj:
                            if ban['is_permanent']:
                                # ban permanente, lo kikko
                                print "perban per %s. kick" % (player.guid)
                                self.rc.putMessage(player.slot, "You are ^1permbanned!")                                
                                self.rc.putMessage(player.slot, "Reason: ^1" + str(ban['ban_reason']))
                                self.rc.putCommand('kick %d' % player.slot)
                            else:
                                c = time.strptime(str(ban['created']),"%Y-%m-%dT%H:%M:%S")
                                t = time.mktime(c)
                                t = t + (int(ban['ban_minute'])*60)
                                t = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(t))
                                if t >= str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")):
                                    print "tempban con scadenza %s per %s. kick" % (t, player.guid)
                                    self.rc.putMessage(player.slot, "You are ^1tempbanned!")                                     
                                    self.rc.putMessage(player.slot, "Reason: ^1" + str(ban['ban_reason']))
                                    self.rc.putCommand("kick %d" % (player.slot))
                                else:
                                    print "tempban scaduto il %s per %s" % (t, player.guid)
                    else:
                        print 'player isn\'t banned'
                        


    def evaluate_command(self, x):

        for searchstring, replacestring in settings.REPLACE_STRINGS:
            x = x.replace(searchstring, replacestring)

        res = re.search( r"(?P<say>say(team)?): (?P<id>\d+) .*?: (?P<text>.*)",x)
        if res or True:
            slot= res.group("id")
            message = res.group("text")
            say = res.group("say")

            # '\n'
            # 'verifico se mi e\' stato passato un comando'
            data = message.split()
            for command, command_prop in settings.COMMANDS.items():
                if data[0] == command_prop['command'] or data[0] == command_prop['command_slug']:
                    # 'e\' un comando, verifico se il player ha i permessi'
                    player = self.rc.getPlayer(res.group("id"))
                    is_authorized = False
                    if player and player.guid != '':
                        player_found, player_obj = self.api.get_player(player.guid)
                        if player_found:
                            if player_obj['level'] >= command_prop['min_level']:
                                is_authorized = True

                        if is_authorized:
                            # 'e\' autorizzato ... perform command'
                            getattr(self.rc, command_prop['function'])(player, message, player_obj)
                        else:
                            self.rc.putMessage(player.slot, settings.MESSAGE_PERMISSION % (command_prop['min_level']))
                    else:
                        # 'no player'
                        pass
            
