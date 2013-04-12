import sys, base64, re, time, optparse
from parser import parser

class Main:

    def __init__(self, argv):

        usage='python2.7 main.py [options]'
        params = optparse.OptionParser(usage)
        params.add_option('-s', '--server_address', help='Server address', dest='server_address')
        params.add_option('-p', '--server_port', help='Server port', dest='server_port')
        params.add_option('-l', '--server_log', help='Server log path', dest='server_log')
        params.add_option('-r', '--rcon_passwd', help='Rcon password encoded base64', dest='rcon_passwd')

        (opts, args) = params.parse_args()

        if opts.server_address is None or opts.server_port is None or opts.server_log is None or opts.rcon_passwd is None:
            print "A mandatory option is missing\n"
            params.print_help()
            exit(-1) 
        else:
            log_parser = parser.Parser(opts.server_log)
            evaluator = parser.Evaluator(opts.server_address, int(opts.server_port), opts.rcon_passwd.decode("base64", "strict"))
            while 1:
                sys.stdout.flush()
                time.sleep(1)

                data = log_parser.read()
                if data is not None:
                    for x in data:
                        if x.find("ClientUserinfo:") != -1 or x.find("ClientUserinfoChanged:")!=-1:
                            """
                            check for existing player and player info
                            """
                            evaluator.evaluate_player(x)
                        elif x.find('say:')!=-1 or x.find('sayteam:')!=-1:
                            """
                            check for bot command
                            """
                            evaluator.evaluate_command(x)


if __name__=="__main__":
    main = Main(sys.argv[1:])
