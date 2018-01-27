#-*- coding: utf-8 -*-
'''
Created on 2015/08/05
@author: m-nakagawa
'''

import re
import urllib

import tornado.gen
import tornado.httpclient
from tornado.options import options

from fos.server.SparqlRequestAgent import postOp
from fos.server.SparqlServerAccess import SparqlServer, SPARQL_JSON, \
    RDF_JSONLD, SelfServer
from fos.sparql.SparqlMorpher import SparqlMorpher


_EqualDivider = re.compile(ur'^\s*(.+?)\s*=\s*(.+)\s*$')


#sys.path.append('../')
#from optparse import TitledHelpFormatter
#tornado.httpclient.AsyncHTTPClient.configure("tornado.curl_httpclient.CurlAsyncHTTPClient")
class MainPageHandler(tornado.web.RequestHandler):
    '''
    Main page.
    '''
    def get( self):
        self.render("index.html")

class GeneratePageHandler(tornado.web.RequestHandler):
    '''
    Main page.
    '''
    def get(self, *args, **kwargs):
        #print args, self.request.host, self.request.path
        #print options.url_prefix
        print args
        rootpath = self.request.host + options.url_prefix
        self.render(args[0], rootpath=rootpath)

class FosRequestHandler(tornado.web.RequestHandler):
    '''
    FOS Request
    '''
    def get( self, param, param2):
        self.render("param_test.html", param=param, param2 = param2)
    
class TestFormHandler(tornado.web.RequestHandler):
    '''
    FOS Request
    '''
    '''
    FOS Request
    '''
    def initialize(self, title):
        self.morph_func = None
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

        method = self.get_argument('method')
        answer_type = self.get_argument('answer_type')
        if answer_type == 'SPARQL':
            accept = ','.join(SPARQL_JSON)
        else:
            accept = ','.join(RDF_JSONLD)
            
        query = self.get_argument('query')

        morph = query

        if method == 'GET':
            req = tornado.httpclient.HTTPRequest(
                                                 url=SelfServer+self.reverse_url('request')+"?"+urllib.urlencode({'query': morph.encode("utf-8")}),
                                                 #body=query,
                                                 #headers={'Accept': 'text/turtle; charset=utf-8', },
                                                 headers={'Accept': accept},
                                                 #proxy_host="proxy",
                                                 #proxy_port=8080
                                                 )
        else:
            req = tornado.httpclient.HTTPRequest(
                                                 url=SelfServer+self.reverse_url('request'),
                                                 body=urllib.urlencode({'query': morph.encode("utf-8")}),
                                                 method='POST',
                                                 #headers={'Accept': 'text/turtle; charset=utf-8', },
                                                 headers={
                                                    'Accept': accept,
                                                    #'Accept': ','.join(_SPARQL_JSON),
                                                    #'Accept': ','.join(_SPARQL_DEFAULT),
                                                    'Content-Type':'application/x-www-form-urlencoded',
                                                 },
                                                 #proxy_host="proxy",
                                                 #proxy_port=8080
                                                 )
            
        httpclient = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(httpclient.fetch, req)
        if response.error:
            response.rethrow()
        #self.set_header('content-type', 'application/atom+xml; charset=UTF-8')
        #self.write(response.body)
        #self.finish()
        self.render("sparqlQuery.html",
                    title= self.title,
                    action = self.request.uri,
                    morph_disp = '',
                    query = query, answer=response.body, server=SparqlServer)
    
class ServiceTestHandler(tornado.web.RequestHandler):
    '''
    Server self access
    '''
    def initialize(self, title):
        self.morph_func = None
        self.title = title
        
    def get(self):
        self.render("testQuery.html",
                    title= self.title,
                    detail='service/',
                    action = self.request.uri,
                    url_param = '',
                    query= '', answer='', server=SparqlServer)
        
    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self):
        method = self.get_argument('method')
        answer_type = self.get_argument('answer_type')
        if answer_type == 'SPARQL':
            accept = ','.join(SPARQL_JSON)
        else:
            accept = ','.join(RDF_JSONLD)
            
        query = self.get_argument('query')
        detail = self.get_argument('service_detail')
        lines = query.splitlines()
        params = {}
        disp_params = ""
        for ln in lines:
            m = _EqualDivider.match(ln)
            if m is not None:
                params[m.group(1).encode("utf-8")] = m.group(2).encode("utf-8")
                disp_params += "%s=%s\n" %(m.group(1),m.group(2))
                
        encoded_params = urllib.urlencode(params)
        url=SelfServer+options.url_prefix+'/'+detail
        
        #print "-----------------------------------------"
        #print query
        #print detail
        #print url

        if method == 'GET':
            url_param = url+'?'+encoded_params
            req = tornado.httpclient.HTTPRequest(
                                                 url=url_param,
                                                 #body=query,
                                                 #headers={'Accept': 'text/turtle; charset=utf-8', },
                                                 headers={'Accept': accept},
                                                 #proxy_host="proxy",
                                                 #proxy_port=8080
                                                 )
        else:
            url_param = url
            req = tornado.httpclient.HTTPRequest(
                                                 url=url,
                                                 body=encoded_params,
                                                 method='POST',
                                                 #headers={'Accept': 'text/turtle; charset=utf-8', },
                                                 headers={
                                                    'Accept': accept,
                                                    #'Accept': ','.join(_SPARQL_JSON),
                                                    #'Accept': ','.join(_SPARQL_DEFAULT),
                                                    'Content-Type':'application/x-www-form-urlencoded',
                                                 },
                                                 #proxy_host="proxy",
                                                 #proxy_port=8080
                                                 )
            
        httpclient = tornado.httpclient.AsyncHTTPClient()
        response = yield tornado.gen.Task(httpclient.fetch, req)
        if response.error:
            response.rethrow()
        #self.set_header('content-type', 'application/atom+xml; charset=UTF-8')
        #self.write(response.body)
        #self.finish()
        self.render("testQuery.html",
                    title= self.title,
                    detail=detail,
                    action = self.request.uri,
                    url_param = url_param,
                    query = disp_params, answer=response.body, server=SparqlServer)


  
class SparqlQueryTestHandler(tornado.web.RequestHandler):
    '''
    FOS Request
    '''
    def initialize(self, title):
        self.morph_func = None
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
        method = self.get_argument('method')
        answer_type = self.get_argument('answer_type')
        if answer_type == 'SPARQL':
            accept = ','.join(SPARQL_JSON)
        else:
            accept = ','.join(RDF_JSONLD)
            
        query = self.get_argument('query')
            
        morph_disp, answer = yield postOp(self.morph_func, 'sparql', 'query', query, method, accept, require_morph_disp=True)
        #morph_disp = rslt[0]
        #answer = rslt[1]
            
        self.render("sparqlQuery.html",
                    title= self.title,
                    action = self.request.uri,
                    morph_disp = morph_disp,
                    query = query, answer=answer, server=SparqlServer)
        
    def set_morph_function(self, func):
        self.morph_func = func
        pass
    
class SparqlQueryMorphHandler(SparqlQueryTestHandler):
    def initialize(self, title):
        super(SparqlQueryMorphHandler, self).initialize(title)
        self.set_morph_function(SparqlMorpher.morph)
    



        
