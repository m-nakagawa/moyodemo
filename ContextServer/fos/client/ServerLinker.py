#-*- coding: utf-8 -*-
'''
Created on 2015/09/09

@author: m-nakagawa
'''
from ws4py.client.tornadoclient import TornadoWebSocketClient
from tornado import ioloop

#_Base = "http://aitc.dyndns.org/openmasami/link"
#_Base = "http://localhost:3030/test/sparql"
_Base = "ws://localhost:8000/" + "openmasami/link"

class MyClient(TornadoWebSocketClient):
    def opened(self):
        for i in range(0, 200, 25):
            self.send("*" * i)

    def received_message(self, m):
        print m
        if len(m) == 175:
            self.close(reason='Bye bye')

    def closed(self, code, reason=None):
        ioloop.IOLoop.instance().stop()

ws = MyClient( _Base, protocols=['http-only', 'chat'])
ws.connect()

ioloop.IOLoop.instance().start()