import time, sys, re, math
from quake3 import pyquake3 as quake
from kgb import settings as settings
from database import api
import random
from random import choice
from geoip import geocode

class Rcon:

    def __init__(self, host_address, host_port, rcon_passwd, api_url , api_user, api_key, geo_database):
        self.host_address = host_address
        self.host_port = host_port
        self.rcon_passwd = rcon_passwd

        self.api_url = api_url
        self.api_user = api_user
        self.api_key = api_key
        self.api = api.Api(api_user, api_key, api_url)

        self.geo_database = geo_database
        self.geocode = geocode.GeoCode(geo_database)

        self.b_balance = False

    def getPlayer(self, slot):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        a.rcon_update()
        p = a.rcon_dumpuser(slot)
        a.connection.close()
        return p   

    def getPlayerSlot(self, data):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        a.rcon_update()
        slot = -1
        count = 0
        
        try: data=int(data)
        except: pass
        if not isinstance(data, int):
            for p in a.players:
                if p.name.lower().find(data.lower())!=-1:
                   count += 1
                   slot =  p.slot
        else:
            for p in a.players:
                if p.slot == data:
                   count += 1
                   slot =  p.slot
        a.connection.close()
        if count == 0 or count > 1:
            return None, False
        return True, slot

    def getFullPlayer(self, data):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        a.rcon_update()
        slot = -1
        count = 0
        p_found, p_slot = self.getPlayerSlot(data)
        if p_found:
            return True, a.rcon_dumpuser(p_slot)
        else:
            return None, False

    def getVariable(self, var):
        s_var = self.putCommand(var)
        s_var = s_var[1].split()[1].replace("is:", "").replace("\"", "")
        replacestrings = [
            ("^1","")
            ,("^2","")
            ,("^3","")
            ,("^4","")
            ,("^5","")
            ,("^6","")
            ,("^7","")
            ,(",","")
        ]
        for searchstring, replacestring in replacestrings:
            s_var = s_var.replace(searchstring, replacestring)
        return s_var      

    def getPlayers(self):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        a.rcon_update()
        a.rcon_dumpuser_all()
        return a.players                

    def evaluateGears(self):
        gearCounter = math.pow(2,len(settings.GEARS))-1

        for i in range(0,len(settings.GEARS)):
            if settings.GEARS[i][2]:
                gearCounter -= settings.GEARS[i][1]
        return gearCounter


    def putCommand(self, data):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        return a.rcon_command(data)

    def putMessage(self, slot, data):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        if slot is not None:
            a.rcon_command('tell %d "%s%s%s"' % (slot, settings.BOT_PREFIX, settings.BOT_MESSAGES_COLOR_PREFIX, data))
        else:
            a.rcon_command('say "%s%s%s"' % (settings.BOT_PREFIX, settings.BOT_MESSAGES_COLOR_PREFIX, data))

    def putBigMessage(self, data):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        a.rcon_command('bigtext "%s"' % (data))

    def version(self, *args, **kwargs):
        self.putMessage(None, settings.MESSAGE_VERSION)

    def help(self, *args, **kwargs):
        admin = args[0]
        data = args[1]
        admin_obj = args[2]

        print 'admin is %s and command is %s' % (admin.name, data)
        received_command = []
        received_command = data.split()
        
        for command, command_prop in settings.COMMANDS.items():
            # for exclude_command in settings.EXCLUDE_COMMANDS:
            #    # print exclude_command
            #    # print command_prop['command']
            #     if command_prop['command'] == str(exclude_command):
            #         break
            if len(received_command) == 1 and int(admin_obj['level'])>=command_prop['min_level']:
                self.putMessage(admin.slot, '%s (%s). %s' % (command_prop['command'], command_prop['command_slug'], command_prop['syntax']))
                time.sleep(1)
            elif len(received_command) == 2 and int(admin_obj['level'])>=command_prop['min_level']:
                if received_command[1] == command or received_command[1] == command_prop['command'].replace('!!', '') or received_command[1] == command_prop['command_slug'].replace('!!', ''):
                    self.putMessage(admin.slot, '%s (%s). %s' % (command_prop['command'], command_prop['command_slug'], command_prop['syntax']))
                    time.sleep(1)


    def bslap(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            player_found, player_slot = self.getPlayerSlot(command[1])
            if player_found:
                for slap in range(1,30):
                    self.putCommand('slap %d' % player_slot)
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])

    def slap(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            player_found, player_slot = self.getPlayerSlot(command[1])
            if player_found:
                self.putCommand('slap %d' % player_slot)
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])

    def kick(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:                
            player_found, player_slot = self.getPlayerSlot(command[1])
            if player_found:
                self.putCommand('kick %d' % player_slot)
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])

    def nuke(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:        
            player_found, player_slot = self.getPlayerSlot(command[1])
            if player_found:
                self.putCommand('nuke %d' % player_slot)
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])

    def mute(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            player_found, player_slot = self.getPlayerSlot(command[1])
            if player_found:
                self.putCommand('mute %d' % player_slot)
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])

    def stop(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        # print command
        if len(command) == 1:
            self.putMessage(None, settings.BOT_MESSAGE_STOP)
            time.sleep(1)
            sys.exit(1)
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])             

    def bomb(self, *args, **kwargs):

        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if settings.BOMB_ACTIVE:
            self.putMessage(admin.slot, "bomb is already active!")
        else:
            if len(command) == 2:
                player_found, player = self.getFullPlayer(command[1])
                if player_found:
                    self.putBigMessage("^7INCOMING!: Bomb has been planted!!!")
                    time.sleep(2)
                    self.putBigMessage("^1%s ^7you have 30sec to defuse the Bomb!" % player.name) 
                    time.sleep(2)
                    self.putBigMessage("^7Wires Are: RED - YELLOW - GREEN - FEAR")
                    time.sleep(2)
                    self.putBigMessage("^7Use: !!wire <color here>")
                    time.sleep(2)
                    settings.BOMB_ACTIVE = True
                    settings.BOMB_SECONDS = 0
                    settings.BOMBED_PLAYER = player
                    settings.BOMBER_ADMIN = admin
                    settings.BOMB_COLOR = choice(['RED', 'YELLOW', 'GREEN', 'FEAR'])
                    # print settings.BOMB_COLOR
                else:
                    self.putMessage(admin.slot, "player doesn't exist or too many player")
            else:
                help_command = '!!help %s' % command[0].replace('!!', '')
                self.help(args[0], help_command, args[2])            

    def wire(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        if not settings.BOMB_ACTIVE:
            self.putMessage(admin.slot, "Bomb is not active!")
        else:
            command = command.split()
            if len(command) == 2:
                if int(admin.slot) == settings.BOMBED_PLAYER.slot:
                    if command[1].lower() == settings.BOMB_COLOR.lower():
                        self.putBigMessage("^7Good Job ^1%s!!! ^7You are right!" % settings.BOMBED_PLAYER.name)
                        time.sleep(2)
                        self.putBigMessage("^1%s ^7you've ^1Failed!!!" % settings.BOMBER_ADMIN.name)
                        time.sleep(2)
                        self.putCommand('slap %d' % int(settings.BOMBER_ADMIN.slot))
                    else:
                        self.putBigMessage("^1%s ^7you've ^1Failed!!!" % settings.BOMBED_PLAYER.name)
                        time.sleep(2)
                        for slap in range(1,30):
                            self.putCommand('slap %d' % settings.BOMBED_PLAYER.slot)
                else:
                    self.putMessage(int(admin.slot), "You are not bombed player")
                    time.sleep(1)
                    self.putCommand('slap %d' % int(admin.slot))

                settings.BOMB_ACTIVE = False
                settings.BOMB_SECONDS = 0
                settings.BOMBED_PLAYER = None
                settings.BOMBER_ADMIN = None                        
            else:
                help_command = '!!help %s' % command[0].replace('!!', '')
                self.help(args[0], help_command, args[2])      

    def tell(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split(None, 2)
        if len(command) == 3:
            player_found, player_slot = self.getPlayerSlot(command[1])
            if player_found:
                self.putMessage(player_slot, "^1" + admin.name + ": ^7" + command[2])
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                

    def say(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split(None, 1)
        if len(command) == 2:
            msg = "^1" + admin.name + ": ^7" + command[1]
            self.putMessage(None, msg)
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                            

    def bigtext(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split(None, 1)
        if len(command) == 2:
            msg = "^7" + command[1]
            self.putBigMessage(msg)
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                                        

    def shuffle(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            self.putCommand('shuffleteams')
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                                                    

    def reload(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            self.putCommand('reload')
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                                                                

    def restart(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            self.putCommand('restart')
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                                                                            

    def cyclemap(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            self.putCommand('cyclemap')
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                                                                                        

    def forceteam(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 3:
            if command[2].lower() not in ["red", "blue", "spec"]:
                self.putMessage(admin.slot, "available parameters are: red|blue|spec")
            else:
                player_found, player_slot = self.getPlayerSlot(command[1])
                if player_found:
                    if command[2].lower() not in ["red", "blue", "spec"]:
                        self.putMessage(admin.slot, "available parameters are: red|blue|spec")
                    else:
                        if command[2] == "spec": command[2] = "spectator"
                        self.putCommand("forceteam %d %s" % (player_slot, command[2]))
                else:
                    self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])             

    def nextmap(self, *args, **kwargs):

        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) in [1,2]:

            if len(command) == 1:
                map = self.getVariable("g_nextmap")
                if map != "":
                    self.putMessage(admin.slot, "Next map is " + map)
                else:
                    self.putMessage(admin.slot, "No next map. you need to set? use !!nextmap <mapname>")
            else:
                cmaps = self.putCommand("dir map bsp")
                found = False
                count = 0
                s_map = ""
                for maps in cmaps:
                    if maps != "print":
                        maps = maps.split()
                        for map in maps:
                            if map.startswith("/"):
                                if map.replace("/", "").replace(".bsp", "") == command[1]:
                                    count = 1
                                    s_map = command[1]
                                    break
                                if map.replace("/", "").replace("ut4_", "").replace(".bsp", "").find(command[1])!=-1:
                                    count += 1
                                    s_map += map.lstrip("/").replace(".bsp", "") + " | "
                if count > 1:
                    self.putMessage(admin.slot, "too many maps with this name: %s" % s_map.rstrip(" | "))
                elif count == 1:
                    self.putMessage(None, "Changing next map ...")
                    time.sleep(1)
                    self.putCommand("g_nextmap " + s_map.strip(" | "))
                    self.putMessage(None, "Next Map is %s" % s_map.strip(" | "))
                else:
                    self.putMessage(admin.slot, "no map with this name")            

        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2]) 

    def maps(self, *args, **kwargs):

        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            cmaps = self.putCommand("dir map bsp")
            smaps = ""
            for maps in cmaps:
                if maps != "print":
                    maps = maps.split()
                    maps.sort()
                    count = 0
                    for map in maps:
                        if map.startswith("/"):
                            count += 1
                            smaps += "^7 | ^2" + map.replace("/", "").replace("ut4_", "").replace(".bsp", "")
                            if count == 5:
                                count = 0
                                smaps = smaps.lstrip(" | ")
                                self.putMessage(admin.slot, smaps)
                                smaps = ""
                                time.sleep(1)
                    if smaps!= "":
                        smaps = smaps.lstrip(" | ")
                        self.putMessage(admin.slot, smaps)                     
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2]) 



    def map(self, *args, **kwargs):

        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            cmaps = self.putCommand("dir map bsp")
            found = False
            count = 0
            s_map = ""
            for maps in cmaps:
                if maps != "print":
                    maps = maps.split()
                    for map in maps:
                        if map.startswith("/"):
                            if map.replace("/", "").replace(".bsp", "") == command[1]:
                                count = 1
                                s_map = command[1]
                                break
                            if map.replace("/", "").replace("ut4_", "").replace(".bsp", "").find(command[1])!=-1:
                                count += 1
                                s_map += map.lstrip("/").replace(".bsp", "") + " | "
            if count > 1:
                self.putMessage(admin.slot, "too many maps with this name: %s" % s_map.rstrip(" | "))
            elif count == 1:
                self.putMessage(None, "Changing map ...")
                time.sleep(1)
                self.putCommand("g_nextmap " + s_map.strip(" | "))
                self.putCommand("cyclemap")
            else:
                self.putMessage(admin.slot, "no map with this name")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2]) 


    def moon(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            if command[1].lower() not in ["on", "off"]:
                self.putMessage(admin.slot, "available parameters are: on|off")
            else:
                if command[1] == "on":
                    self.putCommand("g_gravity 100")
                    self.putBigMessage(settings.MESSAGE_MOONON)
                else:
                    self.putCommand("g_gravity 800")
                    self.putBigMessage(settings.MESSAGE_MOONOFF)
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])  

    def weap(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            if command[1].lower() not in ["+nade", "-nade", "+snipers", "-snipers", "+spas", "-spas", "+pistols", "-pistols", "+automatic", "-automatic", "+negev", "-negev", "all", "none"]:
                self.putMessage(admin.slot, "available parameters are: +/-nade||+/-snipers||+/-spas|+/-pistols|+/-automatic|+/-negev|all|none")
            else:
                param = ""
                value = ""
                if command[1].startswith("+"):
                    param = "+"
                    value = re.findall(r'[+-](\w+)', command[1])[0]
                elif command[1].startswith("-"):
                    param = "-"
                    value = re.findall(r'[+-](\w+)', command[1])[0]
                for i in range(0,len(settings.GEARS)):
                    if settings.GEARS[i][0] == value:
                        if param == "+":
                            settings.GEARS[i][2] = True
                        else:
                            settings.GEARS[i][2] = False
                if command[1] in ["all", "none"]:
                    for i in range(0,len(settings.GEARS)):
                        if command[1]=="all":
                            settings.GEARS[i][2] = True
                        else:
                            settings.GEARS[i][2] = False
                gear = self.evaluateGears()
                self.putCommand("g_gear %d" % int(gear))
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])  


    def cfg(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            cconfs = self.putCommand("dir . cfg")
            sconfs = ""
            for confs in cconfs:
                if confs != "print":
                    confs = confs.split()
                    confs.sort()
                    count = 0
                    for conf in confs:
                        if conf.startswith("uz"):
                            count += 1
                            sconfs += "^7 | ^2" + conf.replace(".cfg", "")
                            if count == 5:
                                count = 0
                                sconfs = sconfs.lstrip(" | ")
                                self.putMessage(admin.slot, sconfs)
                                sconfs = ""
                                time.sleep(1)
                    if sconfs!= "":
                        sconfs = sconfs.lstrip(" | ")
                        self.putMessage(admin.slot, sconfs)
        elif len(command) == 2:
            if command[1] == "default":
                self.putCommand("exec server.cfg")
                #self.putMessage(int(slot), "cfg loaded. use ^2!!reload^7 to reload")
                return True
            bconf = False
            cconfs = self.putCommand("dir . cfg")
            sconfs = ""
            for confs in cconfs:
                if confs != "print":
                    confs = confs.split()
                    confs.sort()
                    count = 0
                    for conf in confs:
                        if conf.startswith("uz"):
                            if conf.replace(".cfg", "") == command[1]:
                                bconf = True
                                self.putCommand("exec %s" % conf)
                                self.putMessage(admin.slot, "cfg loaded. use ^2!!reload^7 to reload")
                                #self.putCommand("reload")
            if not bconf:
                self.putMessage(admin.slot, "cfg doesn't exist")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])  

    def close(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            if settings.SERVER_CLOSED != 'YES':
                passwd = random.randint(1000,9999)
                self.putCommand('g_password "%d"' % passwd)
                self.putMessage(admin.slot, "The server is now protected with password: ^1%s. Please type !!reload to force password" % str(passwd))
                time.sleep(1)
                self.putMessage(admin.slot, "Remember to type ^1!!open^7 before leaving the server")
                #self.putCommand('g_password "%d"' % passwd)
            else:
                self.putMessage(admin.slot, "The server is already protected with password")
      
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])              

    def open(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            self.putCommand('g_password ""')
            self.putMessage(admin.slot, "The server is now without password")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])               

    def teams(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            self.b_balance = False
            self.balance()
            if self.b_balance:
                self.putMessage(admin.slot, "Teams are now balanced")
            else:
                self.putMessage(admin.slot, "Teams are already balanced")
            self.b_balance = False
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])   

    def balance(self):
        replacestrings = [
            ("^1","")
            ,("^2","")
            ,("^3","")
            ,("^4","")
            ,("^5","")
            ,("^6","")
            ,("^7","")
            ,(",", "")
        ]

        red_scores = 0
        blue_scores = 0
        red_numbers = 0
        blue_numbers = 0
        spectator_numbers = 0
        move_red = False
        move_blue = False

        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        a.rcon_update()

        status, data = a.rcon_command("players")
        data = data.strip().split("\n")
        variables = {}

        for record in data:
            try:
                separated = record.strip().split(None, 1)
                key = separated[0].strip()
                value = separated[1].strip()
                variables[key] = value
            except:
                pass

        teams = variables["Scores:"]
        red_scores = int(teams.split()[0].split(":")[1])
        blue_scores = int(teams.split()[1].split(":")[1])

        g_redteamlist = a.rcon_command("g_redteamlist")
        g_redteamlist = g_redteamlist[1].split()[1].replace("is:", "").replace("\"", "")
        for searchstring, replacestring in replacestrings:
            g_redteamlist = g_redteamlist.replace(searchstring, replacestring)

        g_blueteamlist = a.rcon_command("g_blueteamlist")
        g_blueteamlist = g_blueteamlist[1].split()[1].replace("is:", "").replace("\"", "")
        for searchstring, replacestring in replacestrings:
            g_blueteamlist = g_blueteamlist.replace(searchstring, replacestring)

        letters2slots = {'A': '0', 'C': '2', 'B': '1', 'E': '4', 'D': '3', 'G': '6', 'F': '5', 'I': '8', 'H': '7', 'K': '10', 'J': '9', 'M': '12', 'L': '11', 'O': '14', 'N': '13', 'Q': '16', 'P': '15', 'S': '18', 'R': '17', 'U': '20', 'T': '19', 'W': '22', 'V': '21', 'Y': '24', 'X': '23', 'Z': '25'}

        players = a.players
        for player in a.players:
            for letter in g_redteamlist:
                #print letters2slots[letter]
                if int(letters2slots[letter]) == player.slot:
                    player.team = "RED"
                    #red_scores += player.frags
                    red_numbers += 1
                    continue
            for letter in g_blueteamlist:
                if int(letters2slots[letter]) == player.slot:
                    player.team = "BLUE"
                    #blue_scores += player.frags
                    blue_numbers += 1
                    continue
            if player.team is None:
                player.team = "SPECTATOR"
                spectator_numbers += 1

            #print player.name + "[" + player.team + "]" + str(player.frags)

        #print "red score: " + str(red_scores)
        #print "blue score: " + str(blue_scores)

        diffred = red_numbers - blue_numbers
        diffblue = blue_numbers - red_numbers

        if red_numbers + blue_numbers < 2:
            pass
            # print "meno di 2 giocatori, niente da bilanciare"
        elif red_numbers == blue_numbers:
            pass
            # print "numero giocatori uguale, niente da bilanciare"
        else:
            if diffred == 1:
                if red_scores - blue_scores >= 2:
                    # print "punteggio red maggiore di 2, sposto il giocatore + scarso da red a blue"
                    self.score_balance(players, "RED", "BLUE")
                    self.b_balance = True
                else:
                    pass
                    # print "diffred == 1, differenza punteggio red->blue <= 2, niente da bilanciare"
            elif diffblue == 1:
                if blue_scores - red_scores >= 2:
                    # print "punteggio blue maggiore di 2, sposto il giocatore + scarso da blue a red"
                    self.b_balance = True
                    self.score_balance(players, "BLUE", "RED")
                else:
                    pass
                    # print "diffblue == 1, differenza punteggio <= 2, niente da bilanciare"
            elif diffred > 0 and diffred % 2 == 0:
                # print "effettuo team balance sul team red"
                self.b_balance = True
                self.score_balance(players, "RED", "BLUE")
            elif diffblue > 0 and diffblue % 2 == 0:
                # print "effettuo team balance sul team blue"
                self.b_balance = True
                self.score_balance(players, "BLUE", "RED")
            elif diffred > 0 and diffred % 2 != 0:
                # print "effettuo team balance sul team red"
                self.b_balance = True
                self.score_balance(players, "RED", "BLUE")
                # print "rivaluto altri spostamenti"
                self.balance()
            elif diffblue > 0 and diffblue % 2 != 0:
                # print "effettuo team balance sul team blue"
                self.b_balance = True
                self.score_balance(players, "BLUE", "RED")
                # print "rivaluto altri spostamenti"
                self.balance()


    def score_balance(self, players, deflating_team, inflating_team):
        bad_score = 9999
        bad_player_slot = -1

        for player in players:
            if player.team == deflating_team:
                if player.frags < bad_score:
                    bad_player_slot = player.slot
                    bad_score = player.frags
        if bad_player_slot != -1:
            # print "sposto il player + scarso con slot %d" % bad_player_slot
            # print "forceteam %d %s" % (bad_player_slot, inflating_team)
            self.putCommand("forceteam %d %s" % (bad_player_slot, inflating_team)) 

    def tdj(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            if command[1].lower() == 'on':
                seconds = 10
                pseconds = 0
                while pseconds <= seconds:
                    if seconds >= 5:
                        color = '^2'
                    elif seconds < 5 and seconds > 2:
                        color = '^3'
                    else:
                        color = '^1'
                    self.putBigMessage("%sActivating Team Death Jump, please save your position now!!! %s" % (color,seconds))
                    seconds -= 1
                    time.sleep(1)
                self.putCommand('g_respawnprotection 0')
                self.putCommand('g_gear 0')
                self.putCommand('sv_allowLoadPosition 0')
                self.putCommand('sv_regainStamina 0')
                self.putCommand('bigtext "^1Team Death Jump Activated, ENJOY!!!"')
                self.putCommand('restart')
            elif command[1].lower() == 'off':
                seconds = 10
                pseconds = 0
                while pseconds <= seconds:
                    if seconds >= 5:
                        color = '^1'
                    elif seconds < 5 and seconds > 2:
                        color = '^3'
                    else:
                        color = '^2'
                    self.putBigMessage("%sDeactivating Team Death Jump!!! %s" % (color,seconds))
                    seconds -= 1
                    time.sleep(1)
                self.putCommand('g_respawnprotection 9999999')
                self.putCommand('g_gear 63')
                self.putCommand('sv_allowLoadPosition 1')
                self.putCommand('sv_regainStamina 1')
                self.putCommand('bigtext "^1Team Death Jump Deactivated, ENJOY!!!"')
                self.putCommand('restart')
            else:
                self.putMessage(admin.slot, "available parameters are: on|off")                  
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])    

    def alias(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            player_found, player_obj = self.getFullPlayer(command[1])
            if player_found:
                alias_found, alias_objs = self.api.get_aliases(player_obj.guid)
                if alias_found:
                    s_aliases = ''
                    if alias_objs['meta']['total_count'] == 0:
                        self.putMessage(admin.slot, "player doesn't have aliases")
                    else:
                        for item in alias_objs['objects']:
                            s_aliases += item['alias'] + ' | '
                        self.putMessage(admin.slot, str(s_aliases).rstrip(" | "))
                else:
                    self.putMessage(admin.slot, "player doesn't have aliases")       
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")                          
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])    

    def admins(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            players = self.getPlayers()
            s_admins = ""
            s_count = 0
            for player in players:
                player_found = None
                player_obj = None
                player_found, player_obj = self.api.get_player(player.guid)
                if player_found:
                    if player_obj['level'] > 0:
                        s_count += 1
                        s_admins += player_obj['name'] + "(" + str(player_obj['level']) + ")" + " | "
                    if s_count == 5:
                        s_count = 0
                        self.putMessage(admin.slot, str(s_admins).rstrip(" | "))
                        s_admins = ""
            if s_count > 0:
                self.putMessage(admin.slot, str(s_admins).rstrip(" | "))

        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                                               

    def putgroup(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 3:
            if command[2] in ['0', '20', '40', '60', '80', '100']:
                player_found, player_obj = self.getFullPlayer(command[1])
                if player_found:
                    updated_player, updated_player_obj = self.api.update_player_level(player_obj.guid, int(command[2]))
                    if updated_player:
                        self.putMessage(admin.slot, settings.ADMIN_LEVEL_GRANTED_SUCCESSFULLY)
                        if int(command[2]) == 0:
                            self.putMessage(int(player_obj.slot), settings.ADMIN_LEVEL_REMOVED % admin.name)
                        elif int(command[2]) == 20:
                            self.putMessage(int(player_obj.slot), settings.ADMIN_LEVEL_FRIEND)
                        else:
                            self.putMessage(int(player_obj.slot), settings.ADMIN_LEVEL_GRANTED % command[2])
                            self.putMessage(int(player_obj.slot), settings.ADMIN_LEVEL_GRANTED2)      
                else:
                    self.putMessage(admin.slot, "player doesn't exist or too many player") 
            else:
                self.putMessage(admin.slot, "available levels are: 0|20|40|60|80|100")                                           
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])        

    def tempban(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split(None, 3)
        if len(command) == 4:
            try:
                command[2] = int(command[2])
                player_found, player_obj = self.getFullPlayer(command[1])
                if player_found:
                    ban_player = self.api.insert_ban(player_obj, command[3], command[2], 0, admin.name) 
                    if ban_player:
                        self.putMessage(None, "%s banned player %s for %d minutes (reason: %s)" % (admin.name, player_obj.name, int(command[2]), command[3]))

                        self.putCommand("kick %d" % player_obj.slot) 
                    else:
                        self.putMessage(admin.slot, "player %s isn't temp banned" % player_obj.name)   
                else:
                    self.putMessage(admin.slot, "player doesn't exist or too many player") 
            except:
                self.putMessage(admin.slot, "you must specify number for minutes")                                           
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                      

    def permban(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split(None, 2)
        if len(command) == 3:
            
            player_found, player_obj = self.getFullPlayer(command[1])
            if player_found:
                ban_player = self.api.insert_ban(player_obj, command[2], 0, 1, admin.name) 
                if ban_player:
                    self.putMessage(None, "%s permbanned player %s (reason: %s)" % (admin.name, player_obj.name, command[2]))
                    self.putCommand("kick %d" % player_obj.slot) 
                else:
                    self.putMessage(admin.slot, "player %s isn't permbanned" % player_obj.name)   
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player") 
                                              
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])   

    def locate(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 2:
            player_found, player_obj = self.getFullPlayer(command[1])
            if player_found:
                try:
                    geo_address = self.geocode.getInfoFromIP(player_obj.address.split(":")[0])
                    # print geo_address
                    city = str(geo_address['city'])
                    country = str(geo_address['country_name'])
                    
                    if city!="" and country!="":
                        self.putMessage(admin.slot, "%s comes from %s (%s)" % (player_obj.name, city, country))
                    elif city!="" and country=="":
                        self.putMessage(admin.slot, "%s comes from %s" % (player_obj.name, city))
                    elif city=="" and country!="":
                        self.putMessage(admin.slot, "%s comes from %s" % (player_obj.name, country))
                    else:
                        self.putMessage(admin.slot, "I don't know where player from")
                except:
                    self.putMessage(admin.slot, "Cannot locate this player")
            else:
                self.putMessage(admin.slot, "player doesn't exist or too many player")
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])

    def veto(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        if len(command) == 1:
            self.putCommand('veto')
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])                