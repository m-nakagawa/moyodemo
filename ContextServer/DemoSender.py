#-*- coding: utf-8 -*
'''
Created on 2015/09/14

@author: m-nakagawa
'''
import time
import urllib

from tornado import ioloop
from ws4py.client.tornadoclient import TornadoWebSocketClient


class MyClient(TornadoWebSocketClient):
    def opened(self):
        cnt = 0
        while True:
            cnt += 1
            self.send(str(cnt))
            print cnt
            time.sleep(1)

    def received_message(self, m): 
        print m
        pass

    def closed(self, code, reason=None):
        ioloop.IOLoop.instance().stop()

    
_Base = u"ws://localhost:8000/openmasami/"
#_Base = u"ws://aitc.dyndns.org/openmasami/"
_Query = u"stream/ws/record/1F/居間/温度"
if __name__ == '__main__':
    #print u'てすと'
    #print urllib.quote(u'てすと'.encode('utf-8'))
    #print urllib.quote(_Base)
    #exit(1)
    ws = MyClient(_Base+urllib.quote(_Query.encode('utf-8')), protocols=['http-only', 'chat'])

    ws.connect()
    ioloop.IOLoop.instance().start()

    