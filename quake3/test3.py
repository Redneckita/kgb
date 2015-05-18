import threading
import time


def do_stuff(self, *args):

    getattr(rc, 'print2')('player', 'message', 'player_obj')
    time.sleep(5)
    print 'esco da thread'




class Rcon:
	
    def print2(self, *args):
        
        # print args[0], args[1], args[2]
        pass






threads = {}

rc = Rcon()    
t = threading.Thread(target=do_stuff, args=(rc, 'print2',))
t.start()

threads['123'] = t

print threads['123']

time.sleep(10)

lt = threads['123']

if lt.isAlive:
	print 'vivo'
else:
	print 'morto'


