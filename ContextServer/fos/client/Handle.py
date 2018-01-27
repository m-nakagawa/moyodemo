# -*- coding: utf-8 -*-
'''
Created on 2015/04/14

@author: m-nakagawa
'''
import codecs
import json
import sys
import urllib

from tornado.httpclient import HTTPRequest, HTTPClient
from tornado.log import app_log

from fos.server.SparqlServerAccess import SparqlServerQuery, SparqlServerUpdate


#_Base = "http://aitc.dyndns.org/openmasami/request"
#_Base = "http://localhost:3030/test/sparql"
_Base = "http://localhost:8000/" + "openmasami/request"

class Handle(object):
    @classmethod
    def getHandle(cls,direct = False, for_update=False):
        if direct:
            if for_update:
                return _DirectHandleForUpdate
            else:
                return _DirectHandle
        else:
            if for_update:
                return _BaseHandleForUpdate
            else:
                return _BaseHandle
        
    def __init__(self, fos_url):
        self.fos_url = fos_url
        self.client = HTTPClient()
        
    def select(self, query):
        param = urllib.urlencode({'query': query.encode('utf_8')})
        headers = {'Accept':'application/sparql-results+json,application/ld+json,application/json'}
        request = HTTPRequest(self.fos_url+'?'+param,method='GET',headers=headers)
        response = self.client.fetch(request)
        app_log.debug("Result:%s", response.body)
        return json.loads(response.body)
    
    def construct(self, query):
        return self.select(query)
    
    def apply(self, query):
        return self.select(query)
    
    def update(self, query):
        param = urllib.urlencode({'update': query.encode('utf_8')})
        request = HTTPRequest(self.fos_url,method='POST',body=param)
        response = self.client.fetch(request)
        return response.body


_BaseHandle = Handle(_Base)
_BaseHandleForUpdate = Handle(_Base)
_DirectHandle = Handle(SparqlServerQuery)
_DirectHandleForUpdate = Handle(SparqlServerUpdate)


if __name__ == "__main__":
    if len(sys.argv) < 2:
            query = u"""
# 日本語
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>
PREFIX ha: <http://bizar.aitc.jp/ns/fos/0.1/人間API/>
SELECT ?url
WHERE {
    {
          ?room :場所 :ここ .
          ?room :在室 ?p .
          ?c :主人 ?p .
          ?c ha:テキストメッセージ ?url .
    }
}
"""
    else:
        query = codecs.open(sys.argv[1],'r','utf_8').read()
        #query = open(sys.argv[1]).read()
    #import sys;sys.argv = ['', 'Test.testName']
    h = Handle(_Base)
    for i in range(0,1):
        ans = h.select(query)
        print i
    print json.dumps(ans,encoding="utf-8",ensure_ascii=False,indent=2)

    
    