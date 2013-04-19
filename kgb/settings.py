BOT_NAME = "Klaus BOT"
BOT_VERSION = "0.8"
BOT_PREFIX = "^0[^1KGB^0] "
BOT_MESSAGES_COLOR_PREFIX = "^7"

MESSAGE_VERSION = "This is ^1%s ^7version ^5%s" % (BOT_NAME, BOT_VERSION)
MESSAGE_PERMISSION = "Permission required, minimum level is %s"

SPAM_MESSAGES_TIMEOUT = 180
SPAM_MESSAGES = {}

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
        "syntax": "syntax is !!help <command>",
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
        "min_level": 60,
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
        "min_level": 60,
        "syntax": "syntax is !!mute <playername|id>",
        "function": "mute"
    },                
    "aych": {
        "command": "!!aych",
        "command_slug": "!!y",
        "min_level": 100,
        "syntax": "syntax is !!aych <on|off>",
        "function": "aych"
    },     
}
