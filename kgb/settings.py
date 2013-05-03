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
        "function": "version"
    },
    "help": {
        "command": "!!help",
        "command_slug": "!!h",
        "min_level": 0,
        "syntax": "syntax is !!help or !!help <command>",
        "function": "help"
    },
    "bslap": {
        "command": "!!bslap",
        "command_slug": "!!bs",
        "min_level": 80,
        "syntax": "syntax is !!bslap <playername|id>",
        "function": "bslap"
    },
    "slap": {
        "command": "!!slap",
        "command_slug": "!!s",
        "min_level": 60,
        "syntax": "syntax is !!slap <playername|id>",
        "function": "slap"
    },
    "kick": {
        "command": "!!kick",
        "command_slug": "!!k",
        "min_level": 80,
        "syntax": "syntax is !!kick <playername|id>",
        "function": "kick"
    },
    "nuke": {
        "command": "!!nuke",
        "command_slug": "!!nk",
        "min_level": 60,
        "syntax": "syntax is !!nule <playername|id>",
        "function": "nuke"
    },
    "mute": {
        "command": "!!mute",
        "command_slug": "!!m",
        "min_level": 40,
        "syntax": "syntax is !!mute <playername|id>",
        "function": "mute"
    },                
    "die": {
        "command": "!!die",
        "command_slug": "!!d",
        "min_level": 100,
        "syntax": "syntax is !!die",
        "function": "stop"
    },     
    "bomb": {
        "command": "!!bomb",
        "command_slug": "!!b",
        "min_level": 80,
        "syntax": "syntax is !!bomb <playername|id>",
        "function": "bomb"
    },       
    "wire": {
        "command": "!!wire",
        "command_slug": "!!w",
        "min_level": 0,
        "syntax": "syntax is !!wire <choice>",
        "function": "wire"
    },           
    "tell": {
        "command": "!!tell",
        "command_slug": "!!tl",
        "min_level": 20,
        "syntax": "syntax is !!tell <playername|id> <phrase>",
        "function": "tell"
    },               
    "say": {
        "command": "!!say",
        "command_slug": "!!sy",
        "min_level": 20,
        "syntax": "syntax is !!say <phrase>",
        "function": "say"
    },                   
    "bigtext": {
        "command": "!!bigtext",
        "command_slug": "!!bt",
        "min_level": 40,
        "syntax": "syntax is !!bigtext <phrase>",
        "function": "bigtext"
    },                      
    "shuffle": {
        "command": "!!shuffle",
        "command_slug": "!!sh",
        "min_level": 60,
        "syntax": "syntax is !!shuffle",
        "function": "shuffle"
    },                          
    "restart": {
        "command": "!!restart",
        "command_slug": "!!rs",
        "min_level": 60,
        "syntax": "syntax is !!restart",
        "function": "restart"
    },                          
    "reload": {
        "command": "!!reload",
        "command_slug": "!!rl",
        "min_level": 60,
        "syntax": "syntax is !!reload",
        "function": "reload"
    },                          
    "cyclemap": {
        "command": "!!cyclemap",
        "command_slug": "!!cm",
        "min_level": 60,
        "syntax": "syntax is !!cyclemap",
        "function": "cyclemap"
    },              
    "forceteam": {
        "command": "!!forceteam",
        "command_slug": "!!ft",
        "min_level": 80,
        "syntax": "syntax is !!forceteam <playername|id> <red|blue|spec>",
        "function": "forceteam"
    },                  
    "nextmap": {
        "command": "!!nextmap",
        "command_slug": "!!nm",
        "min_level": 60,
        "syntax": "syntax is !!nextmap or !!nextmap <mapname>",
        "function": "nextmap"
    },                      
    "maps": {
        "command": "!!maps",
        "command_slug": "!!ms",
        "min_level": 20,
        "syntax": "syntax is !!maps",
        "function": "maps"
    },                      
    "map": {
        "command": "!!map",
        "command_slug": "!!mp",
        "min_level": 60,
        "syntax": "syntax is !!map <mapname>",
        "function": "map"
    },                              
    "moon": {
        "command": "!!moon",
        "command_slug": "!!mo",
        "min_level": 60,
        "syntax": "syntax is !!moon <on|off>",
        "function": "moon"
    },             
    "weap": {
        "command": "!!weap",
        "command_slug": "!!wp",
        "min_level": 60,
        "syntax": "syntax is !!weap <+/-^1na^7de|+/-^1sn^7ipers|+/-^1sp^7as|+/-^1pi^7stols|+/-^1au^7tomatic|+/-^1ne^7gev|all|none>",
        "function": "weap"
    },                 
    "cfg": {
        "command": "!!cfg",
        "command_slug": "!!cf",
        "min_level": 80,
        "syntax": "syntax is !!cfg or !!cfg <uz_conf_file>",
        "function": "cfg"
    },                     
    "close": {
        "command": "!!close",
        "command_slug": "!!cl",
        "min_level": 80,
        "syntax": "syntax is !!close",
        "function": "close"
    }, 
    "open": {
        "command": "!!open",
        "command_slug": "!!op",
        "min_level": 80,
        "syntax": "syntax is !!open",
        "function": "open"
    },         
    "teams": {
        "command": "!!teams",
        "command_slug": "!!ts",
        "min_level": 0,
        "syntax": "syntax is !!teams",
        "function": "teams"
    },  
    "tdj": {
        "command": "!!tdj",
        "command_slug": "!!tj",
        "min_level": 80,
        "syntax": "syntax is !!tdj <on|off>",
        "function": "tdj"
    },
    "alias": {
        "command": "!!alias",
        "command_slug": "!!al",
        "min_level": 20,
        "syntax": "syntax is !!alias <playername|id>",
        "function": "alias"
    },   
    "admins": {
        "command": "!!admins",
        "command_slug": "!!ad",
        "min_level": 20,
        "syntax": "syntax is !!admins",
        "function": "admins"
    },  
    "putgroup": {
        "command": "!!putgroup",
        "command_slug": "!!pg",
        "min_level": 100,
        "syntax": "syntax is !!putgroup <playername|id> <level>",
        "function": "putgroup"
    },     
    "tempban": {
        "command": "!!tempban",
        "command_slug": "!!tb",
        "min_level": 60,
        "syntax": "syntax is !!tempban <playername|id> <minutes> <reason>",
        "function": "tempban"
    },  
    "permban": {
        "command": "!!permban",
        "command_slug": "!!pb",
        "min_level": 80,
        "syntax": "syntax is !!permban <playername|id> <reason>",
        "function": "permban"
    }, 
    "locate": {
        "command": "!!locate",
        "command_slug": "!!lc",
        "min_level": 20,
        "syntax": "syntax is !!locate <playername|id>",
        "function": "locate"
    },                     
}

GEARS = [
  ['nade', 1, True]
  ,['snipers',2,True]
  ,['spas',4,True]
  ,['pistols',8,True]
  ,['automatic',16,True]
  ,['negev',32,True]

  ,['na', 1, True]
  ,['sn',2,True]
  ,['sp',4,True]
  ,['pi',8,True]
  ,['au',16,True]
  ,['ne',32,True]  
]

