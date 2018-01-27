# -*- coding: utf-8 -*-
'''
Created on 2015/04/14

@author: m-nakagawa
'''

import codecs
import json
import logging
import re
import sys

from rdflib.graph import Graph

from fos.client.sparqlaccess import SparqlAccess


logging.basicConfig()

#_Base = "http://localhost:3030/test/sparql"
_Base = "http://localhost:8000/" + "openmasami/request"
_Commands = {u'APPLY',u'COMPILE',u'SELECT',u'CONSTRUCT',u'DELETE', u'INSERT'}
_Query_Outer = re.compile(ur"^(.*?)\n\s*("+'|'.join(_Commands)+ur")",re.S+re.M)

def fos_access(query):
    m = _Query_Outer.match(query)
    if m is None:
        print >> sys.stderr, ','.join(_Commands)+u"のいずれかと認識できません。\n"
        exit(1)
        
    sa = SparqlAccess(_Base)
    cmd = m.group(2)
    if cmd in {u'APPLY', u'COMPILE'}:
        results = sa.apply(query)
    elif cmd == u'SELECT':
        results = sa.select(query)
    elif cmd in {u'DELETE', u'INSERT'}:
        results = sa.update(query)
    elif cmd == u'CONSTRUCT':
        results = sa.construct(query)
    else:
        print >> sys.stderr, "BUG"
        exit(1)
    if isinstance(results, Graph):
        s = results.serialize(format='json-ld')
        s = json.loads(s)
        s = json.dumps(s, encoding="utf-8",ensure_ascii=False,indent=2)
    elif isinstance(results, dict):
        s = json.dumps(results,encoding="utf-8",ensure_ascii=False,indent=2)
    else:
        s = results.response.msg
    print s
    #print results
    
    #for result in results["results"]["bindings"]:
    #    print(result["url"]["value"])
        

    pass


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
    fos_access(query)