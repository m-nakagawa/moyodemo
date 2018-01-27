#-*- coding: utf-8 -*-
'''
Created on 2015/09/09

@author: m-nakagawa
'''
import json

from tornado import websocket
from tornado.log import app_log

from fos.server.PathQuery2 import PathQuery2
from fos.server.RecordService2 import add_watcher, remove_watcher, inform_watcher


class WebSocketSubscriber(websocket.WebSocketHandler):
    #def __init__(self, *args, **kwargs):
    #    super(WebSocketSubscriber, self).__init__(*args, **kwargs)

    def initialize(self):
        pass
    
    def open(self, *args):
        self.name = args[0]
        app_log.debug("WebSocket opened:subscribing:%s", self.name)

        command = self.name.split("/")
        self.path_query = PathQuery2(command)
        for idfr in self.path_query.get_idfr():
            app_log.debug("Watching:%s", idfr) 
            add_watcher(idfr, self.watcher)

    def on_message(self, message):
        app_log.debug("Ignore:%s", message)
        pass
        
    def on_close(self):
        app_log.debug("WebSocket closed:%s", self.name)
        
        if self.path_query is not None:
            for idfr in self.path_query.get_idfr():
                remove_watcher(idfr, self.watcher)
        
    def check_origin(self, origin):
        return True
    
    #@gen.coroutine
    def watcher(self, idfr, value):
        app_log.debug("Watcher:%s:%s", self.name, value)
        #ret = {idfr:value}
        ret = value
        self.write_message(json.dumps(ret))
        
class WebSocketRecorder(websocket.WebSocketHandler):
    def initialize(self):
        pass
    
    def open(self, *args):
        self.name = args[0]
        app_log.debug("WebSocket opened:recording:%s", self.name)

        command = self.name.split("/")
        self.path_query = PathQuery2(command)

    def on_message(self, value):
        app_log.debug("value:%s", value)
        for idfr in self.path_query.get_idfr():
            app_log.debug("idfr:%s, value:%s", idfr, value)
            self.path_query.update_value(idfr, value)
            inform_watcher(idfr, value)
            pass

        
    def on_close(self):
        app_log.debug("WebSocket closed:%s", self.name)
        
        
    def check_origin(self, origin):
        return True
    
    #@gen.coroutine
    def watcher(self, idfr, value):
        app_log.debug("Watcher:%s:%s", self.name, value)
        #ret = {idfr:value}
        ret = value
        self.write_message(json.dumps(ret))        