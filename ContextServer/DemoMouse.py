#-*- coding: utf-8 -*
#日本語
'''
Created on 2015/09/14

@author: m-nakagawa
'''
import time
import urllib

from tornado import ioloop
from ws4py.client.tornadoclient import TornadoWebSocketClient

from raspi.MouseReader import MouseReader

_W = [None]
_MReader = None

class MyClient(TornadoWebSocketClient):
    def opened(self):
        cnt = 0
        prev = 0
        while True:
            cnt += 1
            (x,y) = _MReader.get_data()
            now = time.time()
            if now-prev > 0.1:
                if y == 0:
                    print x
                try:
                    self.send(str(x))
                except:
                    print "Exception"
                    self.close_connection()
                    return
                prev = time.time()

    def received_message(self, m): 
        print m
        pass

    def closed(self, code, reason=None):
        print "Closed"
        _W[0] = None
        ioloop.IOLoop.instance().stop()

    
#_Base = u"ws://localhost:8000/openmasami/"
_Base = u"ws://aitc.dyndns.org/openmasami/"
_Query = u"stream/ws/record/1F/居間/温度"
if __name__ == '__main__':
    #print u'てすと'
    #print urllib.quote(u'てすと'.encode('utf-8'))
    #print urllib.quote(_Base)
    #exit(1)
    _MReader = MouseReader()

    while True:
        if _W[0] is None:
            _W[0] = MyClient(_Base+urllib.quote(_Query.encode('utf-8')), protocols=['http-only', 'chat'])
            _W[0].connect()
        ioloop.IOLoop.instance().start()
        

    
