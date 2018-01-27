#-*- coding: utf-8 -*
'''
Created on 2015/09/14

@author: m-nakagawa
'''
import urllib

from tornado import ioloop
from ws4py.client.tornadoclient import TornadoWebSocketClient
#import RPi.GPIO as GPIO
_W = [None,None]

class MyClient(TornadoWebSocketClient):
    def opened(self):
        print "opened:", self.num
        pass

    def received_message(self, m):
        if m.data == '"ON"':
            print self.num, "OK" 
        else:
            print self.num, m.data
        pass

    def closed(self, code, reason=None):
        print "closed", self.num
        _W[self.num-1] = None
        ioloop.IOLoop.instance().stop()

    def set_num(self,num):
        self.num = num
    
#_Base = u"ws://localhost:8000/openmasami/"
_Base = u"ws://aitc.dyndns.org/openmasami/"
_Query1 = u"stream/ws/subscribe/1F/居間/照明"
_Query2 = u"stream/ws/subscribe/2F/居間/照明"
if __name__ == '__main__':
    #print u'てすと'
    #print urllib.quote(u'てすと'.encode('utf-8'))
    #print urllib.quote(_Base)
    #exit(1)
    #GPIO.setmode(GPIO.BCM)
    #GPIO.setup(18,GPIO.OUT)
    #GPIO.setup(23,GPIO.OUT)
    while True:
        if _W[0] is None:
            _W[0] = MyClient(_Base+urllib.quote(_Query1.encode('utf-8')), protocols=['http-only', 'chat'])
            _W[0].set_num(1)
            _W[0].connect()
        
        if _W[1] is None:
            _W[1] = MyClient(_Base+urllib.quote(_Query2.encode('utf-8')), protocols=['http-only', 'chat'])
            _W[1].set_num(2)
            _W[1].connect()
        ioloop.IOLoop.instance().start()
        

    