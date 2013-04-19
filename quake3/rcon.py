import time
from quake3 import pyquake3 as quake
from kgb import settings as settings

class Rcon:

    def __init__(self, host_address, host_port, rcon_passwd):
        self.host_address = host_address
        self.host_port = host_port
        self.rcon_passwd = rcon_passwd

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

    def putCommand(self, data):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        return a.rcon_command(data)

    def putMessage(self, slot, data):
        a = quake.Administrator(self.host_address, self.host_port, self.rcon_passwd)
        if slot is not None:
            a.rcon_command('tell %d "%s%s%s"' % (slot, settings.BOT_PREFIX, settings.BOT_MESSAGES_COLOR_PREFIX, data))
        else:
            a.rcon_command('say "%s%s%s"' % (settings.BOT_PREFIX, settings.BOT_MESSAGES_COLOR_PREFIX, data))

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
            if len(received_command) == 1:
                self.putMessage(admin.slot, '%s (%s) for level %s. %s' % (command_prop['command'], command_prop['command_slug'], command_prop['min_level'], command_prop['syntax']))
            elif len(received_command) == 2:
                if received_command[1] == command or received_command[1] == command_prop['command'].replace('!!', '') or received_command[1] == command_prop['command_slug'].replace('!!', ''):
                    self.putMessage(admin.slot, '%s (%s) for level %s. %s' % (command_prop['command'], command_prop['command_slug'], command_prop['min_level'], command_prop['syntax']))

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
                print 'player non trovato o troppi player con questo nome|id'                
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
                print 'player non trovato o troppi player con questo nome|id'  
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
                print 'player non trovato o troppi player con questo nome|id'  
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
                print 'player non trovato o troppi player con questo nome|id'   
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
                print 'player non trovato o troppi player con questo nome|id'                         
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])

    def aych(self, *args, **kwargs):
        
        admin = args[0]
        command = args[1]
        print 'admin is %s and command is %s' % (admin.name, command)
        command = command.split()
        print command
        if len(command) == 2 and command[1] in ['on', 'off']:
            # comando ok
            print 'eseguo comando'
            if command[1] == 'on':
                print 'on attivo'
            else:
                print 'off disattivo'
        else:
            help_command = '!!help %s' % command[0].replace('!!', '')
            self.help(args[0], help_command, args[2])
    
