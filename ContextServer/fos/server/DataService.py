#-*- coding: utf-8 -*-
'''
Created on 2015/09/01

@author: m-nakagawa
'''
from tornado.log import app_log
import tornado.web

from fos.client.Handle import Handle
from fos.server.SparqlServerAccess import SparqlServerUpdate, SparqlServerQuery

_WatchingRecords = {}

def add_watcher(idfr, func):
    global _WatchingRecords
    app_log.debug("Add watcher:%s", idfr)
    s = _WatchingRecords.get(idfr)
    if s is None:
        s = set()
        _WatchingRecords[idfr] = s
    s.add(func)
    pass
    for k in _WatchingRecords.keys():
        print k


def remove_watcher(idfr, func):
    global _WatchingRecords
    app_log.debug("Remove watcher:%s", idfr)
    s = _WatchingRecords.get(idfr)
    if s is not None and func in s:
        s.remove(func)

def inform_watcher(idfr, value):
    global _WatchingRecords
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

def _update_func(req, command):
    idfr = req.get_argument('idfr', default='')
    if idfr[0] == '"':
        idfr = idfr[1:-1]
    value = req.get_argument('value', default='')

    app_log.debug("DATAUPDATE:%s:%s:%s", command[0], idfr, value )
    inform_watcher(idfr, value)
    
    query = _DatalogQuery % (value, idfr)
    #print query
    h = Handle(SparqlServerUpdate)
    h.update(query)
    # 成功したかどうかは問わない
    return None

def _latest_func(req, command):
    print ','.join(command[1:])
    idfr = req.get_argument('idfr', default='')
    if idfr[0] == '"':
        idfr = idfr[1:-1]
    query = _DatavalueQuery % (idfr)
    app_log.debug("Query:query%s", query)
    h = Handle(SparqlServerQuery)
    ret = h.select(query)
    print ret
    v = ret[u'results'][u'bindings'][0][u'data'][u'value']
    app_log.debug("DATAVALUE:%s:%s:%s", command[0], idfr, v)
    # 成功したかどうかは問わない
    return str(v)

_Services = {
              'update': _update_func, 
              'latest': _latest_func, 

             }

def _web_func(command,params):
    pass

class DataService(tornado.web.RequestHandler):
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
        app_log.debug(args[0])
        command = args[0].split("/")
        func = _Services.get(command[0])
        if func is None:
            raise tornado.web.HTTPError(404)
        
        ret = func(self, command)
        if ret is not None:
            self.write(ret)
        self.finish()
    
