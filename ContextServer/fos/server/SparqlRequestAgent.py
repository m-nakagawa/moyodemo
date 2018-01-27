#-*- coding: utf-8 -*-
'''
Created on 2016/01/05

@author: m-nakagawa
'''
import json
import urllib

from tornado import gen
import tornado.gen

from fos.server.SparqlServerAccess import SparqlServerTrunk


#_SlicingMode = True

@tornado.gen.coroutine
def postOp(morph_func, opath, param_name, query, method, accept, require_morph_disp=False, slicing_mode=True, insert_live_data=True):
    if morph_func is not None:
        if slicing_mode:
            predef, morph = morph_func(query, slicing=True)
        else:
            morph = [morph_func(query, slicing=False)]
            predef = ""
    else:
        morph = [query]
        predef = ""

    morph_disp = ""
    cnt = 0
    values = u""
    while True:
        s = morph[cnt]
        command = predef + s
        if values != u"":
            repl = u"$$$%d$$$" %(cnt)
            print repl
            command = command.replace(repl, values)
            print command
        if require_morph_disp:
            morph_disp += "----\n"+ command
    #--            
    #h = self.request.headers.get('Accept')
    #print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!", h)
    #print(urllib.urlencode({'query': morph.encode("utf-8")}))
    #--            
        
        if method == 'GET':
            req = tornado.httpclient.HTTPRequest(
                                                 url=SparqlServerTrunk+opath+"?"+urllib.urlencode({param_name: command.encode("utf-8")}),
                                                 #body=query,
                                                 #headers={'Accept': 'text/turtle; charset=utf-8', },
                                                 headers={'Accept': accept},
                                                 #proxy_host="proxy",
                                                 #proxy_port=8080
                                                 )
        else:
            req = tornado.httpclient.HTTPRequest(
                                                 url=SparqlServerTrunk+opath,
                                                 body=urllib.urlencode({param_name: command.encode("utf-8")}),
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
        cnt += 1
        if cnt == len(morph):
            break
        print response
        print cnt
        print morph[cnt]
        body = json.loads(response.body)
        variables = body[u"head"][u"vars"]
        results = body[u"results"][u"bindings"]
        values = u"VALUES (?" + u" ?".join(variables) + ") {\n"
        
        for r in results:
            values += u"("
            for k in variables:
                v = r[k][u"value"]
                t = r[k][u"type"]
                if t == u"uri":
                    values += "<"+v+">"
                else:
                    values += str(v)
                values += u" "
                
            values += u")\n"
        values += u"}\n"
        print values
        print "----"

    if require_morph_disp:
        raise gen.Return((morph_disp, response.body))
    else:
        raise gen.Return(response.body)
    