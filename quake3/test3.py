import threading


def do_stuff(self, *args):

    getattr(rc, 'print2')('player', 'message', 'player_obj')

class Rcon:
	
    def print2(self, *args):
        print 'suca'
        print args[0], args[1], args[2]




rc = Rcon()    

t = threading.Thread(target=do_stuff, args=(rc, 'print2',))
t.start()