import threading
import time

class Rcon:
    
    def __init__(self):
        self.threads = {}

    def do_stuff(self, *args):
        try:
            lth = self.threads['123']
            if lth is not None:
                print 'thread exists: ', lth
        except KeyError:
            t = threading.Thread(target=self.do_threaded_stuff)
            t.start()   
            # self.threads['123'] =  t   


    def do_threaded_stuff(self):
        print 'entrato nel thread'
        try:
            print 'provo a cancellare'
            del self.threads['123']
            print 'cancellato'
        except KeyError:
            print 'non esiste'





r = Rcon()
r.do_stuff()        