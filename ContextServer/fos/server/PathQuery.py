#-*- coding: utf-8 -*-
'''
Created on 2015/09/12

@author: masami5
'''
#from tornado.log import app_log

from tornado.log import app_log

from fos.client.Handle import Handle
from fos.server.SparqlServerAccess import SparqlServerQuery, SparqlServerUpdate


class PathQuery(object):
    '''
    classdocs
    '''
    _PREFIX = u"PREFIX %s: <%s>\n"
    _HEAD =(
            u"PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>\n" +
            u"SELECT ?idfr ?update\nWHERE {\n" +
            u"  ?s1 :パス識別子 lcl:%s .\n"
            )
    _TAIL = u"}"
    _BODY =(
            u"  ?s%d ?p%d ?s%d .\n" +
            u"  ?s%d :パス識別子 lcl:%s .\n"
            )
    _LAST =(
            u"  ?s%d :値識別子  ?idfr .\n" +
            u'  OPTIONAL {\n' +
            u'    ?s%d :%s ?update .\n' +
            u'  }\n'
            )
    
    _DATA_HEAD1 =(
                 u"PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>\n" +
                 u"SELECT"
                 )
    _DATA_HEAD2 = u" ?value%d"
    _DATA_HEAD3 =(
                  u"\n"+
                  u"WHERE {\n"
                  )
    _DATA_BODY = (
                  u'  OPTIONAL {\n' +
                  u'    ?s%d :%s ?value%d .\n' +
                  u'  }\n'
                  )
    _DATA_TAIL = (
                  u'}\n'
                  ) 
    
    _UPDATE = (
               u"PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>\n" +
               u"DELETE{ ?s ?p ?olddata . }\n" +
               u'INSERT{ ?s ?p "%s" . }\n' +
               u"WHERE {\n" +
               u'  ?c  :値識別子      "%s" .\n' +
               u"  ?c  :%s  ?p .\n" +
               u"  ?c  :値主        ?s .\n" +
               #u"  ?c    :値更新        :直接 .\n" +
               u"  OPTIONAL { ?s ?p ?olddata . }\n" +
               u"}\n"
               )
    
    _handle = Handle(SparqlServerQuery)
    _handle_update = Handle(SparqlServerUpdate)
    
    def __init__(self, path, namespaces={}):
        '''
        Constructor
        '''
        self.path = path
        if len(path) == 0:
            self.path = [""]
        self.namespaces = namespaces
        self.namespaces["lcl"] = u"http://bizar.aitc.jp/ns/fos/0.1/local#"
        self.idfr_query = self.gen_idfr_query()
        self.reqire_refresh = True
        self.idfr = None
        #self.value_query = None
        
    def refresh(self):
        self.reqire_refresh = False
        self.idfr, self.update = self.refresh_idfr()
        #self.value_query = self.make_value_query()
    
    def get_idfr_query(self):
        return self.idfr_query
    
    def gen_idfr_query(self):
        cnt = len(self.path)
        if cnt >= 1:
            idfr_query = u""
            for prefix, uri in self.namespaces.items():
                idfr_query += PathQuery._PREFIX % (prefix, uri)
            idfr_query += PathQuery._HEAD % self.path[0]
            for i in range(1,cnt-1):
                idfr_query += PathQuery._BODY % (i, i+1, i+1, i+1, self.path[i])
            idfr_query += PathQuery._LAST % (cnt-1, cnt-1, self.path[-1])
            idfr_query += PathQuery._TAIL
        else:
            idfr_query = None
        return idfr_query
    
    def refresh_idfr(self):
        if self.idfr_query is None:
            return self.path[0]
        
        #h = Handle(SparqlServerQuery)
        ret = PathQuery._handle.select(self.idfr_query)
        #app_log.info("%s", str(ret))
        #print ret
        idfr = []
        update = {}
        for d in  ret[u'results'][u'bindings']:
            idf = d[u'idfr'][u'value']
            idfr.append(idf)
            updt = d.get('update')
            if updt is not None:
                update[idf] = updt[u'value']
        #print update[idfr[0]]
        return idfr, update
        
    def get_idfr(self):
        if self.reqire_refresh:
            self.refresh()
        return self.idfr
    
    def make_value_query(self):
        self.value_query = PathQuery._DATA_HEAD1
        for i in range(0,len(self.idfr)):
            self.value_query += PathQuery._DATA_HEAD2 %(i)
        self.value_query += PathQuery._DATA_HEAD3
        for i in range(0,len(self.idfr)):
            self.value_query += PathQuery._DATA_BODY %(i,self.idfr[i],i,i,i,i,i,i,i)
            
        self.value_query += PathQuery._DATA_TAIL
        return self.value_query
    
    def get_value_query(self):
        return self.value_query
    
    def get_values(self):
        if self.reqire_refresh:
            self.refresh()
        print self.value_query
        ans = self._handle.select(self.value_query)
        #print ans
        ret = []
        for v in ans[u'results'][u'bindings'][0].values():
            ret.append(v[u'value'])
        return ret
    
    def update_value(self, idfr, value):
        request = PathQuery._UPDATE % (value, idfr)
        print request
        PathQuery._handle_update.update(request)
        #ret = PathQuery._handle_update.update(request)
        #app_log.debug("Ret:%s", ret)
    
        
if __name__ == '__main__':
    #q = PathQuery([u"1F",u"居間", u"人", u"名前"])
    #q = PathQuery([u"1F",u"居間", u"温度"])
    q = PathQuery([u"2F",u"居間", u"温度"])
    #q = PathQuery([u"people_in_room_01"])
    #q = Pathidfr_query(["1F","居間", "名前"])
    print q.get_idfr_query()
    q.refresh()
    print q.get_idfr()
    print q.get_value_query()
    for v in q.get_values():
        print v
    