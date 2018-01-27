#-*- coding: utf-8 -*-
'''
Created on 2015/08/25

@author: m-nakagawa
'''
import json
import re
import urllib

from tornado.log import app_log
import tornado.web

from fos.server.SparqlRequestAgent import postOp
from fos.server.SparqlServerAccess import RDF_JSONLD, SparqlServer
from fos.sparql.SparqlMorpher import SparqlMorpher


_OK = json.dumps([
                  {
                   "@graph": [
                              {
                               "@id": "_:b0",
                               "http://bizar.aitc.jp/ns/fos/0.1/処理結果": [
                                                                        {
                                                                         "@id": "http://bizar.aitc.jp/ns/fos/0.1/正常"
                                                                         }
                                                                        ]
                               }
                              ],
                   "@id": " "
                   }
                  ],
                  encoding="utf-8",ensure_ascii=False,indent=2)

#from pyld import jsonld
#import pyld
#from rdflib.graph import Graph
_SPARQL_JSON     = ["application/sparql-results+json", "text/javascript", "application/json"]
_Query_Outer = re.compile(r"^(.*)\n\s*(APPLY|COMPILE)\s*\{(.*)\s*}\s*$",re.S+re.M)
_Update_Outer = re.compile(r"^(.*)\n\s*(DELETE|INSERT)",re.S+re.M)
_Split_Construct = re.compile(r"CONSTRUCT")
_Find_Where = re.compile(r"WHERE", re.M)

# 同じキーがあると上書き！！！！！
def json_extend(dst,ext):
    for e in ext:
        idk = e.get('@id')
        if idk in dst:
            dst[idk].update(e)
        else:
            dst[idk] = e

@tornado.gen.coroutine
def _ext_apply(m):      
    if True:
        prefix = m.group(1)
        div = _Split_Construct.split(m.group(3))[1:]
        #div = [div[0]]
        
        
        accept = ','.join(RDF_JSONLD)
        answer = {} # @id:パラメータ
        context = {}
        for d in div:
            if _Find_Where.search(d) is None:
                d = d + "WHERE {}"
            q = prefix + "CONSTRUCT" + d
            #print "------"
            #print q
            #print "------"
        
            req = tornado.httpclient.HTTPRequest(
                                                 url=SparqlServer,
                                                 body=urllib.urlencode({'query': q.encode("utf-8")}),
                                                 method='POST',
                                                 #headers={'Accept': 'text/turtle; charset=utf-8', },
                                                 headers={
                                                          'Accept': accept,
                                                          'Content-Type':'application/x-www-form-urlencoded',
                                                          },
                                                 #proxy_host="proxy",
                                                 #proxy_port=8080
                                                 )
            
            httpclient = tornado.httpclient.AsyncHTTPClient()
            response = yield tornado.gen.Task(httpclient.fetch, req)
            if response.error:
                response.rethrow()
            data = response.body
            data = unicode(data,'utf-8')
            #print data
            
            #g = Graph().parse(data=data, format='json-ld')
            #print "xxxxx--"
            #print( g.serialize(format='json-ld', indent=4))
            js = json.loads(data)
            #exjs = jsonld.expand(js)
            #print "yyyyy--"
            #print( json.dumps(js, indent=2))
            context.update(js['@context'])
            del js['@context']
            if '@graph' in js:
                array = js['@graph']
            else:
                array = [js]
            
            json_extend(answer,array)
            #print "answer=", answer
            
        if len(answer) == 1:
            ans = answer.values()[0]
            ans['@context'] = context
        else:
            ans = {'@graph':answer, '@context':context}
        raise tornado.gen.Return(ans)         
                   
class FosRequestSender(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    '''
    FOS Request
    '''
    def initialize(self, title):
        self.title = title
        
    def get(self):
        self.render("sparqlQuery.html",
                    title= self.title,
                    morph_disp = "",
                    action = self.request.uri,
                    query= '', answer='', server=SparqlServer)
        
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
            
        query = self.get_argument('query')

        m = _Query_Outer.match(query)
        if m is None:
            raise Exception("Syntax??")
        ans = yield _ext_apply(m)
 

        answer = json.dumps(ans,encoding="utf-8",ensure_ascii=False,indent=2)
        morph_disp = ""
        self.render("sparqlQuery.html",
                    title= self.title,
                    action = self.request.uri,
                    morph_disp = morph_disp,
                    query = query, answer=answer, server=SparqlServer)
        

class SparqlQueryHandler(tornado.web.RequestHandler):
    def initialize(self):
        #self.morph_func = None
        self.morph_func = SparqlMorpher.morph

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        #print self.request
        #print "!!SparqlQueryHandler:", self.request.method
    
        accept = self.request.headers.get('Accept')
        if accept is None:
            accept = 'application/sparql-results+json,application/ld+json,application/json'
        #print accept
        #accept = ','.join(SPARQL_JSON)
        #accept = ','.join(RDF_JSONLD)
        app_log.debug("Accept:%s", accept)
        app_log.debug("Header:%s", str(self.request.headers))
            
        args = self.get_arguments('query')
        if len(args) != 0:
            query = args[-1]
        else:
            query = self.get_argument('update')
            
        #print query
        
        m = _Query_Outer.match(query)
        if m is not None:
            # APPLY文のとき
            yield self.apply(m)

        else:
            if  _Update_Outer.match(query):
                # updateはまだ権限チェック対象外
                morph_func = None
                #morph = query
                opath = "update"
                param_name = "update"
            else:
                morph_func = self.morph_func
                opath = "sparql"
                param_name = "query"
                #if self.morph_func is not None:
                #    morph = self.morph_func(query)
                #else:
                #    morph = query

            #answer = yield postOp(morph_func, opath, param_name, query, 'POST', accept, require_morph_disp=False)
            answer = yield postOp(morph_func, opath, param_name, query, 'GET', accept, require_morph_disp=False)

#             req = tornado.httpclient.HTTPRequest(
#                                                  url=SparqlServerTrunk+opath,
#                                                  body=urllib.urlencode({param_name: morph.encode("utf-8")}),
#                                                  method='POST',
#                                                  headers={
#                                                           'Accept': accept,
#                                                           #'Accept': ','.join(_SPARQL_JSON),
#                                                           #'Accept': ','.join(_SPARQL_DEFAULT),
#                                                           'Content-Type':'application/x-www-form-urlencoded',
#                                                           },
#                                                  #proxy_host="proxy",
#                                                  #proxy_port=8080
#                                                  )
#             httpclient = tornado.httpclient.AsyncHTTPClient()
#             response = yield tornado.gen.Task(httpclient.fetch, req)
#             if response.error:
#                 response.rethrow()

            #self.set_header('content-type', 'application/atom+xml; charset=UTF-8')
            #self.set_header('content-type', 'application/ld+json; charset=UTF-8')
            #print response.body
            #print response.headers.get('Content-type')
            
            self.write(answer)
            #for (k, v) in response.headers.get_all():
            #    print "------%s:%s" % (k,v)
            #    self.set_header(k,v)
            #self.set_header('Content-type', 'application/ld+json; charset=UTF-8')
            #self.set_header('Content-type', 'application/json; charset=UTF-8')
            #self.set_header('Content-type', 'application/sparql-results+json; charset=utf-8')
            #self.set_header('Content-type', response.headers.get('Content-type'))
            #self.set_header('Fuseki-Request-ID', 30 )
            #self.set_header('Cache-Control', 'must-revalidate,no-cache,no-storeFuseki-Request-ID' )
            #self.set_header('Pragma', 'no-cache')
            #self.set_header('Transfer-Encoding', 'chunked')
            #self.set_header('Server', 'Fuseki (2.0.0)')
            
        self.finish()
    
    @tornado.gen.coroutine
    def apply(self,m):
        ans = yield _ext_apply(m)
        if m.group(2) == 'APPLY':
            # 実行結果は隠す
            yield self.remote_exec(ans)
            
            self.write(_OK)
            self.set_header('Content-type', 'application/ld+json; charset=UTF-8')

        else:
            answer = json.dumps(ans,encoding="utf-8",ensure_ascii=False,indent=2)
            self.write(answer)
            self.set_header('Content-type', 'application/ld+json; charset=UTF-8')
            #self.set_header('Content-type', 'application/json; charset=UTF-8')
        
        
    @tornado.gen.coroutine
    def remote_exec(self,query):
        #print "-------------------------------------"
        print json.dumps(query,encoding="utf-8",ensure_ascii=False,indent=2)
        dst = query.get(u"宛先")
        if dst is None:
            raise tornado.gen.Return()
        del query[u"宛先"]
        query_str = json.dumps(query,encoding="utf-8",ensure_ascii=False,indent=2).encode('utf-8')
        for url in dst:
            print url
            req = tornado.httpclient.HTTPRequest(
                                                 url=url,
                                                 body=urllib.urlencode({'params': query_str}),
                                                 method='POST',
                                                 headers={
                                                    'Content-Type':'application/x-www-form-urlencoded',
                                                 },
                                                 #proxy_host="proxy",
                                                 #proxy_port=8080
                                                 )
            
            httpclient = tornado.httpclient.AsyncHTTPClient()
            response = yield tornado.gen.Task(httpclient.fetch, req)
            if response.error:
                app_log.debug(response)
          
        
    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self):
        self.post()
        #h = self.request.headers.get('Accept')
        #print("get:!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", h)
        #response = { 'id': 123,
        #             'name': 'Crazy Game',}
        #self.write(response)
        #self.finish()
    
