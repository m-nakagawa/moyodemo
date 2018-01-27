# -*- coding: utf-8 -*-
'''
Created on 2015/04/14

@author: m-nakagawa
'''

import sys
print sys.path

from fos.client.sparqlaccess import SparqlAccess


base = "http://localhost:3030/test/sparql"
#base = "http://localhost:8000/" + "openmasami/request"

def testGet():
    sa = SparqlAccess(base)
    query = """
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
    results = sa.select(query)
    print results
    
    #for result in results["results"]["bindings"]:
    #    print(result["url"]["value"])
        

    pass


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    testGet()