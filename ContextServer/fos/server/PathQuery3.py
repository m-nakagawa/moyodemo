#-*- coding: utf-8 -*-
'''
Created on 2015/09/12

@author: masami5
'''
from tornado.log import app_log
import tornado.options

from fos.client.Handle import Handle


#from fos.server.SparqlServerAccess import SparqlServerQuery, SparqlServerUpdate
class PathQuery3(object):
    '''
    classdocs
    '''
    _PREFIX = u"PREFIX %s: <%s>\n"
    _HEAD =(
            u"PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>\n" +
            u"SELECT ?idfr\nWHERE {\n" +
            u"  ?s1 :パス識別子 lcl:%s .\n"
            )
    _TAIL = u"}"
    _BODY =(
            u"  ?s%d ?p%d ?s%d .\n" +
            u"  ?s%d :パス識別子 lcl:%s .\n"
            )
    _LAST =(
            u"  ?s%d :%s ?idfr .\n"
            )
    

    
    
    def __init__(self, path, direct=True, path_namespace=None):
        '''
        Constructor.
        Arguments:
        path -- Query path string.
        direct -- True: Direct connect to the real RDF store.
        path_namespace -- The namespace of path keywords.
        '''
        self.handle = Handle.getHandle(direct=direct)
        self.path = path
        if len(path) == 0:
            self.path = [""]
        self.namespaces = {}
        if path_namespace is None:
            self.namespaces["lcl"] = u"http://bizar.aitc.jp/ns/fos/0.1/local/"
        else:
            self.namespaces["lcl"] = path_namespace
        self.idfr_query = self.gen_idfr_query()
        self.reqire_refresh = True
        self.idfr = None
        self.value_query = None
        
    def refresh(self):
        """Refresh the idfr.
        """
        self.reqire_refresh = False
        self.idfr = self.refresh_idfr()
    
    def get_idfr_query(self):
        return self.idfr_query
    
    def gen_idfr_query(self):
        cnt = len(self.path)
        if cnt > 1:
            idfr_query = u""
            for prefix, uri in self.namespaces.items():
                idfr_query += PathQuery3._PREFIX % (prefix, uri)
            idfr_query += PathQuery3._HEAD % self.path[0]
            for i in range(1,cnt-1):
                idfr_query += PathQuery3._BODY % (i, i+1, i+1, i+1, self.path[i])
            idfr_query += PathQuery3._LAST % (cnt-1,self.path[-1])
            idfr_query += PathQuery3._TAIL
        else:
            idfr_query = None
        return idfr_query
    
    def refresh_idfr(self):
        if self.idfr_query is None:
            return self.path[0]
        
        #h = Handle(SparqlServerQuery)
        ret = self.handle.select(self.idfr_query)
        #app_log.info("%s", str(ret))
        #print ret
        idfr = []
        for d in  ret[u'results'][u'bindings']:
            idf = d[u'idfr'][u'value']
            if d[u'idfr'][u'type'] == 'uri':
                idfr.append(idf)
                #updt = d.get('update')
                #if updt is not None:
                #    update[idf] = updt[u'value']
            else:
                app_log.debug("Found idfr is not uri: %s :\n%s\n" % (idf, self.idfr_query))
        #print update[idfr[0]]
        return idfr
        
    def get_idfr(self):
        if self.reqire_refresh:
            self.refresh()
        return self.idfr
    
    def databese_maybe_changed(self):
        self.reqire_refresh = True
        
if __name__ == '__main__':
    tornado.options.parse_command_line()
    
    #q = PathQuery([u"1F",u"居間", u"人", u"名前"])
    #q = PathQuery([u"1F",u"居間", u"温度"])
    q = PathQuery3([u"2F",u"居間", u"温度"], direct=True)
    #q = PathQuery([u"people_in_room_01"])
    #q = Pathidfr_query(["1F","居間", "名前"])
    print q.get_idfr_query()
    q.refresh()
    print q.get_idfr()
