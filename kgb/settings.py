BOT_NAME = "Klaus BOT"
BOT_VERSION = "2.0 Beta"
BOT_PREFIX = "^0[^1KGB^0] "
BOT_MESSAGES_COLOR_PREFIX = "^7"
BOT_MESSAGE_STOP = "KGB stops reading your logs..."
BOT_MESSAGE_START = "KGB started reading your logs!!"

# BOT MESSAGES
MESSAGE_VERSION = "This is ^1%s ^7version ^5%s" % (BOT_NAME, BOT_VERSION)
MESSAGE_PERMISSION = "Permission denied, minimum required level is %s"
MESSAGE_MOONON = "^1Fly me to the Moon..."
MESSAGE_MOONOFF = "^2Welcome back to Earth!"
ADMIN_LEVEL_GRANTED_SUCCESSFULLY = "Level granted!^3"
ADMIN_LEVEL_REMOVED = "Admin ^3%s ^7took all your rights, you are now at Level ^30"
ADMIN_LEVEL_FRIEND = "You are now ^3Friend^7.^3"
ADMIN_LEVEL_GRANTED = "Admin level ^3%s ^7granted! Be careful!^3"
ADMIN_LEVEL_GRANTED2 = "With great power comes great responsibility. Be careful!^3"

SPAM_MESSAGES_TIMEOUT = 180
SPAM_MESSAGES = []

EXCLUDE_COMMANDS = []

SERVER_CLOSED = "NO"
SERVER_CLOSED_TIMEOUT = 180

BOMB_ACTIVE = None
BOMB_SECONDS = None
BOMBED_PLAYER = None
BOMB_COLOR = None
BOMBER_ADMIN = None

REPLACE_STRINGS = [
    ("^1","")
    ,("^2","")
    ,("^3","")
    ,("^4","")
    ,("^5","")
    ,("^6","")
    ,("^7","")
]

COMMANDS = {
    "version": {
        "command": "!!version",
        "command_slug": "!!v",
        "min_level": 0,
        "syntax": "syntax is !!version",
        "description": "Print bot version",
        "function": "version"
    },
    "help": {
        "command": "!!help",
        "command_slug": "!!h",
        "min_level": 0,
        "syntax": "syntax is !!help <command>",
        "description": "Display commands list and specific help for a command",
        "function": "help"
    },
    "bslap": {
        "command": "!!bslap",
        "command_slug": "!!bs",
        "min_level": 80,
        "syntax": "syntax is !!bslap <playername|id>",
        "description": "Bitchslap to death a player",
        "function": "bslap"
    },
    "slap": {
        "command": "!!slap",
        "command_slug": "!!s",
        "min_level": 60,
        "syntax": "syntax is !!slap <playername|id>",
        "description": "Slap a player",
        "function": "slap"
    },
    "kick": {
        "command": "!!kick",
        "command_slug": "!!k",
        "min_level": 60,
        "syntax": "syntax is !!kick <playername|id>",
        "description": "Kick a player from the server",
        "function": "kick"
    },
    "nuke": {
        "command": "!!nuke",
        "command_slug": "!!nk",
        "min_level": 60,
        "syntax": "syntax is !!nuke <playername|id>",
        "description": "Nuke a player",
        "function": "nuke"
    },
    "mute": {
        "command": "!!mute",
        "command_slug": "!!m",
        "min_level": 40,
        "syntax": "syntax is !!mute <playername|id>",
        "description": "Mute a player (toggle mute status)",
        "function": "mute"
    },                
    "die": {
        "command": "!!die",
        "command_slug": "!!d",
        "min_level": 100,
        "syntax": "syntax is !!die",
        "description": "Shutdown (and possibly restart) the bot",
        "function": "stop"
    },     
    "bomb": {
        "command": "!!bomb",
        "command_slug": "!!b",
        "min_level": 80,
        "syntax": "syntax is !!bomb <playername|id>",
        "description": "Place a bomb that a player must defuse in 30 seconds, if player fails he get bitchslapped",
        "function": "bomb"
    },       
    "wire": {
        "command": "!!wire",
        "command_slug": "!!w",
        "min_level": 0,
        "syntax": "syntax is !!wire <color>",
        "description": "Use it to choose a wire to defuse a bomb",
        "function": "wire"
    },           
    "tell": {
        "command": "!!tell",
        "command_slug": "!!tl",
        "min_level": 20,
        "syntax": "syntax is !!tell <playername|id> <phrase>",
        "description": "Tell something to a player in private (no public/team chat)",
        "function": "tell"
    },               
    "say": {
        "command": "!!say",
        "command_slug": "!!sy",
        "min_level": 20,
        "syntax": "syntax is !!say <phrase>",
        "description": "Talk to people, useful when you are in spectator mode",
        "function": "say"
    },                   
    "bigtext": {
        "command": "!!bigtext",
        "command_slug": "!!bt",
        "min_level": 40,
        "syntax": "syntax is !!bigtext <phrase>",
        "description": "Print a big centered text in the screen",
        "function": "bigtext"
    },                      
    "shuffle": {
        "command": "!!shuffle",
        "command_slug": "!!sh",
        "min_level": 60,
        "syntax": "syntax is !!shuffle",
        "description": "Shuffle (randomize) the teams",
        "function": "shuffle"
    },                          
    "restart": {
        "command": "!!restart",
        "command_slug": "!!rs",
        "min_level": 60,
        "syntax": "syntax is !!restart",
        "description": "Restart the game (not the bot)",
        "function": "restart"
    },                          
    "reload": {
        "command": "!!reload",
        "command_slug": "!!rl",
        "min_level": 60,
        "syntax": "syntax is !!reload",
        "description": "Reload the game (not the bot)",
        "function": "reload"
    },                          
    "cyclemap": {
        "command": "!!cyclemap",
        "command_slug": "!!cm",
        "min_level": 60,
        "syntax": "syntax is !!cyclemap",
        "description": "Cycle to the next map in map cycle",
        "function": "cyclemap"
    },              
    "forceteam": {
        "command": "!!forceteam",
        "command_slug": "!!ft",
        "min_level": 80,
        "syntax": "syntax is !!forceteam <playername|id> <red|blue|spec>",
        "description": "Force a player in a team or in spectator mode",
        "function": "forceteam"
    },                  
    "nextmap": {
        "command": "!!nextmap",
        "command_slug": "!!nm",
        "min_level": 60,
        "syntax": "syntax is !!nextmap or !!nextmap <mapname>",
        "description": "Display or set the next map in cycle",
        "function": "nextmap"
    },                      
    "maps": {
        "command": "!!maps",
        "command_slug": "!!ms",
        "min_level": 20,
        "syntax": "syntax is !!maps",
        "description": "Print available maps list",
        "function": "maps"
    },                      
    "map": {
        "command": "!!map",
        "command_slug": "!!mp",
        "min_level": 60,
        "syntax": "syntax is !!map <mapname>",
        "description": "Immediately change map",
        "function": "map"
    },                              
    "moon": {
        "command": "!!moon",
        "command_slug": "!!mo",
        "min_level": 60,
        "syntax": "syntax is !!moon <on|off>",
        "description": "Lower gravity to g_gravity 100 (on) or raise it back to 800 (off)",
        "function": "moon"
    },             
    "weap": {
        "command": "!!weap",
        "command_slug": "!!wp",
        "min_level": 60,
        "syntax": "syntax is !!weap <+/-^1na^7de|+/-^1sn^7ipers|+/-^1sp^7as|+/-^1pi^7stols|+/-^1au^7tomatic|+/-^1ne^7gev|all|none>",
        "description": "Weapon limiter, useful to set up a game for restricted weapons usage (i.e.: Pistols and nades only)",
        "function": "weap"
    },                 
    "cfg": {
        "command": "!!cfg",
        "command_slug": "!!cf",
        "min_level": 80,
        "syntax": "syntax is !!cfg or !!cfg <uz_conf_file>",
        "description": "Load a UZ configuration file, if no parameter is given the bot will list all available UZ config files",
        "function": "cfg"
    },                     
    "close": {
        "command": "!!close",
        "command_slug": "!!cl",
        "min_level": 80,
        "syntax": "syntax is !!close",
        "description": "Close the server for PCW. Generates a random 4 digit password and gives it to the caller and stops the spamming of messages. When the server is empty the bot re-open it automatically. It's magic!",
        "function": "close"
    }, 
    "open": {
        "command": "!!open",
        "command_slug": "!!op",
        "min_level": 80,
        "syntax": "syntax is !!open",
        "description": "Force re-opening of the server (clears password and start spamming messages again)",
        "function": "open"
    },         
    "teams": {
        "command": "!!teams",
        "command_slug": "!!ts",
        "min_level": 0,
        "syntax": "syntax is !!teams",
        "description": "Do a team balance based upon score",
        "function": "teams"
    },  
    "tdj": {
        "command": "!!tdj",
        "command_slug": "!!tj",
        "min_level": 80,
        "syntax": "syntax is !!tdj <on|off>",
        "description": "Activate Team Death Jump mode (for jump servers). Server is reset and respawn protection is zeroed, all weapons available to all players... have fun!",
        "function": "tdj"
    },
    "alias": {
        "command": "!!alias",
        "command_slug": "!!al",
        "min_level": 20,
        "syntax": "syntax is !!alias <playername|id>",
        "description": "Print all known aliases for a player",
        "function": "alias"
    },   
    "admins": {
        "command": "!!admins",
        "command_slug": "!!ad",
        "min_level": 20,
        "syntax": "syntax is !!admins",
        "description": "Print a list of connected admins and their levels",
        "function": "admins"
    },  
    "putgroup": {
        "command": "!!putgroup",
        "command_slug": "!!pg",
        "min_level": 100,
        "syntax": "syntax is !!putgroup <playername|id> <level>",
        "description": "Change a player's group, useful to make friends, recruits, junior and senior admins on the fly",
        "function": "putgroup"
    },     
    "tempban": {
        "command": "!!tempban",
        "command_slug": "!!tb",
        "min_level": 60,
        "syntax": "syntax is !!tempban <playername|id> <minutes> <reason>",
        "description": "Temporarily ban a player specifying the duration in minutes and a reason for the ban",
        "function": "tempban"
    },  
    "permban": {
        "command": "!!permban",
        "command_slug": "!!pb",
        "min_level": 80,
        "syntax": "syntax is !!permban <playername|id> <reason>",
        "description": "Permanently ban a player with a reason",
        "function": "permban"
    },      
    "locate": {
        "command": "!!locate",
        "command_slug": "!!lc",
        "min_level": 20,
        "syntax": "syntax is !!locate <playername|id>",
        "description": "Locate a player at city level (if available, otherwise displays the Country)",
        "function": "locate"
    },               
    "veto": {
        "command": "!!veto",
        "command_slug": "!!vt",
        "min_level": 60,
        "syntax": "syntax is !!veto",
        "description": "cancel vote in progress",
        "function": "veto"
    },      
}

# GEARS = [
#   ['nade', 1, True, 'na']
#   ,['snipers',2,True, 'sn']
#   ,['spas',4,True, 'sp']
#   ,['pistols',8,True, 'pi']
#   ,['automatic',16,True, 'au']
#   ,['negev',32,True, 'ne']

#   # ,['na', 1, True]
#   # ,['sn',2,True]
#   # ,['sp',4,True]
#   # ,['pi',8,True]
#   # ,['au',16,True]
#   # ,['ne',32,True]  
# ]


GEARS = [
    ['pistols', 'FGfg', True]
    ,['smg', 'IJh', True]
    ,['autos', 'LMae', True]
    ,['spas', 'H', True]
    ,['negev', 'c', True]
    ,['snipers', 'NZ', True]
    ,['nades', 'OQK', True]
    ,['armor', 'RW', True]
    ,['attachments', 'UV', True]
    ,['extras', 'XTS', True]
]

