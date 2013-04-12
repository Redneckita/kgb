API_URL = 'http://kgb-test.rkf-clan.org/api/v1/'
API_USER = 'rkf_test'
API_KEY = '64738'
API_USER_RESOURCE_URI = '/api/v1/user/3/'
API_SERVER_RESOURCE_URI = '/api/v1/server/2/'


BOT_NAME = "Klaus BOT"
BOT_VERSION = "0.8"
BOT_PREFIX = "^0[^1KGB^0] "
BOT_MESSAGES_COLOR_PREFIX = "^7"


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
}
