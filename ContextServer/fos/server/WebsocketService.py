#-*- coding: utf-8 -*-
'''
Created on 2015/09/09

@author: m-nakagawa
'''
import json

from tornado import websocket
from tornado.log import app_log

from fos.server.DataService import add_watcher, remove_watcher


class EchoWebSocket(websocket.WebSocketHandler):
    def open(self):
        print "WebSocket opened"

    def on_message(self, message):
        self.write_message(u"You said: " + message)

    def on_close(self):
        print "WebSocket closed"
        
    def check_origin(self, origin):
        return True
    
    
class DatalinkWebSocket(websocket.WebSocketHandler):
    def initialize(self):
        self.watching = set()
    
    def open(self):
        print "WebSocket opened"
        self.write_message('{"people_in_room_01":1212}')

    def on_message(self, message):
        app_log.debug("Websocket msg:%s", message)
        q = json.loads(message)
        req = q.get("subscribe")
        if req is not None:
            if type(req) is not list:
                req = [req]
            for idfr in req:
                app_log.debug("Addwatcher:%s", idfr)
                add_watcher(idfr, self.watcher)
                self.watching.add(idfr)
        
    def on_close(self):
        print "WebSocket closed"
        for idfr in self.watching:
            remove_watcher(idfr, self.watcher)
        
    def check_origin(self, origin):
        return True
    
    #@gen.coroutine
    def watcher(self, idfr, value):
        app_log.debug("Watcher:%s", value)
        ret = {idfr:value}
        self.write_message(json.dumps(ret))