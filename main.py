import sys, base64, re, time, optparse
from parser import parser
from kgb import settings as settings
from quake3 import pyquake3 as quake

class Main:

    def __init__(self, argv):

        usage='python2.7 main.py [options]'
        params = optparse.OptionParser(usage)
        params.add_option('-s', '--server_address', help='Server address', dest='server_address')
        params.add_option('-p', '--server_port', help='Server port', dest='server_port')
        params.add_option('-l', '--server_log', help='Server log path', dest='server_log')
        params.add_option('-r', '--rcon_passwd', help='Rcon password encoded base64', dest='rcon_passwd')
        params.add_option('-u', '--api_url', help='url for json api, ask to klaus@rkf-klan.org', dest='api_url')
        params.add_option('-a', '--api_user', help='user for json api, ask to klaus@rkf-klan.org', dest='api_user')
        params.add_option('-k', '--api_key', help='key for json api, ask to klaus@rkf-klan.org', dest='api_key')
        params.add_option('-d', '--geo_dat', help='geocity database', dest='geo_database')

        (opts, args) = params.parse_args()

        if opts.server_address is None or opts.server_port is None \
            or opts.server_log is None or opts.rcon_passwd is None \
            or opts.api_url is None or opts.api_user is None \
            or opts.api_key is None or opts.geo_database is None:

            # "A mandatory option is missing\n"

            params.print_help()
            exit(-1) 
        else:
            log_parser = parser.Parser(opts.server_log)
            evaluator = parser.Evaluator(opts.server_address, int(opts.server_port), opts.rcon_passwd.decode("base64", "strict"), opts.api_url, opts.api_user, opts.api_key, opts.geo_database)
            evaluator.evaluate_config()

            evaluator.start()
            
            seconds = 0
            check_seconds = 0
            while 1:
                sys.stdout.flush()
                time.sleep(1)

                # SPAM MESSAGES
                seconds += 1
                if int(seconds) == int(settings.SPAM_MESSAGES_TIMEOUT) and len(settings.SPAM_MESSAGES)>0:
                    seconds = 0
                    # check if server is closed
                    a = quake.Administrator(opts.server_address, int(opts.server_port), opts.rcon_passwd.decode("base64", "strict"))
                    g_passwd = a.getVariable("g_password")
                    # if open do spam
                    if g_passwd == "":
                        evaluator.put_spam()

                #check per reset g_password
                check_seconds += 1
                if settings.SERVER_CLOSED != 'YES' and check_seconds == int(settings.SERVER_CLOSED_TIMEOUT):
                    check_seconds = 0
                    a = quake.Administrator(opts.server_address, int(opts.server_port), opts.rcon_passwd.decode("base64", "strict"))
                    a.rcon_update()
                    players = a.players
                    if len(players) == 0:
                        self.putCommand('g_needpass 0')
                        a.rcon_command('g_password ""')
                        a.rcon_command('g_matchmode 0')
                        a.rcon_command('reload')

                # BOMB check
                if settings.BOMB_ACTIVE:
                    settings.BOMB_SECONDS +=1
                    if settings.BOMB_SECONDS == 30:
                        a = quake.Administrator(opts.server_address, int(opts.server_port), opts.rcon_passwd.decode("base64", "strict"))
                        for slap in range(1,30):
                            a.rcon_command('slap %d' % int(settings.BOMBED_PLAYER.slot))
                        settings.BOMB_ACTIVE = False
                        settings.BOMB_SECONDS = 0
                        settings.BOMBED_PLAYER = None
                        settings.BOMBER_ADMIN = None                         
                    elif settings.BOMB_SECONDS == 20:
                        a = quake.Administrator(opts.server_address, int(opts.server_port), opts.rcon_passwd.decode("base64", "strict"))
                        a.rcon_command('bigtext "^710 Seconds Remaining... Come on ^1%s! ^7Its Gunna BLOW !!!"' % settings.BOMBED_PLAYER.name)

                data = log_parser.read()
                if data is not None:
                    for x in data:
                        if x.find("ClientUserinfo:") != -1 or x.find("ClientUserinfoChanged:")!=-1 or x.find("ClientBegin:")!=-1:
                            """
                            check for existing player and player info
                            """
                            try:
                                evaluator.evaluate_player(x)
                            except:
                                pass
                        elif x.find('say:')!=-1 or x.find('sayteam:')!=-1:
                            """
                            check for bot command
                            """
                            try:
                                evaluator.evaluate_command(x)
                            except:
                                pass


if __name__=="__main__":
    main = Main(sys.argv[1:])
