#-*- coding: utf-8 -*-
'''
Created on 2015/09/01

@author: m-nakagawa
'''
import json
import time

from tornado.log import app_log
import tornado.web

from fos.client.Handle import Handle
from fos.server.PathQuery3 import PathQuery3
from fos.server.PhysicalObjects import get_physical_object, refresh_all_sensors


#from fos.server.PathQuery import PathQuery
#from fos.client.Handle import Handle
#from fos.server.SparqlServerAccess import SparqlServerUpdate, SparqlServerQuery
_WatchingRecords = {}
_WatchingValues = {}

#idfrと値の連想配列
_Values = {}



    

def add_watcher(idfr, func):
    #global _WatchingRecords
    app_log.debug("Add watcher:%s", idfr)
    s = _WatchingRecords.get(idfr)
    if s is None:
        s = set()
        _WatchingRecords[idfr] = s
    s.add(func)
    value = _WatchingValues.get(idfr)
    if value is not None:
        func(idfr, value)
    pass
    #for k in _WatchingRecords.keys():
        #print k


def remove_watcher(idfr, func):
    #global _WatchingRecords
    app_log.debug("Remove watcher:%s", idfr)
    s = _WatchingRecords.get(idfr)
    if s is not None and func in s:
        s.remove(func)

def inform_watcher(idfr, value):
    #global _WatchingRecords
    _WatchingValues[idfr] = value
    s = _WatchingRecords.get(idfr)
    #s = _WatchingRecords[idfr]
    #for k in _WatchingRecords.keys():
    #    print k, s, k==s
    if s is not None:
        for f in s:
            f(idfr, value)
            #yield f(idfr, value)

    
_DatalogQuery = u"""
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>
DELETE{ ?c :測定値         ?data . }
INSERT{
    ?c :測定値          %s .
}
WHERE {
    ?c  :値識別子       "%s" .
    OPTIONAL {
        ?c  :測定値         ?data .
    }
}
"""

_DatavalueQuery = u"""
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>
SELECT ?data 
WHERE {
    ?c  :値識別子       "%s" .
    OPTIONAL {
        ?c  :測定値         ?data .
    }
}
"""

#refresh_all_sensors()

def _update_func(req, command):
    path_query = PathQuery3(command[1:],direct=True)
    app_log.debug("Query:query:%s", ','.join(command[1:]))
    value = req.get_argument('value', default='')
    dt = req.get_argument('datetime', default='')
    if dt == "":
        dtime = time.time()
    else:
        dtime = float(dt)
    
    for idfr in path_query.get_idfr():
        o = get_physical_object(idfr)
        print idfr, value
        o.set_scalar_value(dtime, value)
        inform_watcher(idfr, value)
    
    # 成功したかどうかは問わない
    return None

def _latest_func(req, command):
    #print ','.join(command[1:])
    path_query = PathQuery3(command[1:],direct=True)
    app_log.debug("Query:%s", ','.join(command[1:]))
    print path_query.get_idfr_query()
    values = []
    for idfr in path_query.get_idfr():
        o = get_physical_object(idfr)
        values.append(o.get_scalar_value())
    app_log.debug("DATAVALUE:%s", ':'.join(values))
    # 成功したかどうかは問わない
    return str(json.dumps(values))

_Services = {
              'update': _update_func, 
              'latest': _latest_func, 

             }

def _web_func(command,params):
    pass

class DataProxy(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, *args, **kwargs):
        yield self.common(args, kwargs)

    @tornado.web.asynchronous
    @tornado.gen.engine
    def put(self, *args, **kwargs):
        yield self.common(args, kwargs)

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, *args, **kwargs):
        yield self.common(args, kwargs)
    
    @tornado.gen.coroutine    
    def common(self, args, kwargs):
        self.set_header('Access-Control-Allow-Origin', '*')        
        app_log.debug(args[0])
        command = args[0].split("/")
        func = _Services.get(command[0])
        if func is None:
            raise tornado.web.HTTPError(404)
        
        ret = func(self, command)
        if ret is not None:
            self.write(ret)
        self.finish()
    

