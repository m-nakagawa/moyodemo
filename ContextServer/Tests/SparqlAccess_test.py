# -*- coding: utf-8 -*-
'''
Created on 2015/04/14

@author: m-nakagawa
'''
import unittest
from rdf.rdfuploader import RdfUploader
from rdf.sparqlaccess import SparqlAccess

class Test(unittest.TestCase):


    def setUp(self):
        self.base = "http://localhost:3030/"
        self.rdfup = RdfUploader(self.base+"memory/data")
        filename = "data/mysample10.ttl"
        data = open(filename, 'rb').read()
        #r = uploader.data(data, graph=None)
        r = self.rdfup.upload_data(data, graph=u'テスト')
        if r.status_code != 204 and r.status_code != 201 and r.status_code != 200:
            print r.text
            print r.status_code
            self.assertTrue(False)
        pass


    def tearDown(self):
        pass


    def testGet(self):
        sa = SparqlAccess(self.base+"memory/sparql")
        query = """
# 日本語
PREFIX : <http://bizar.aitc.jp/ns/spaceos/0.1/> 
PREFIX ha: <http://bizar.aitc.jp/ns/spaceos/0.1/人間API>
SELECT ?url ?g
WHERE {
      GRAPH ?g {
      ?room :場所 :ここ .
      ?room :在室 ?p .
      ?c :主人 ?p .
      ?c ha:テキストメッセージ ?url .
      }
}
"""
        results = sa.get(query)
        for result in results["results"]["bindings"]:
            print(result["url"]["value"])
            print(result["g"]["value"])

        print "TestGet"
        pass

    def testGet2(self):
        sa = SparqlAccess(self.base+"memory/sparql")
        query = """
# 日本語
PREFIX : <http://bizar.aitc.jp/ns/spaceos/0.1/> 
PREFIX ha: <http://bizar.aitc.jp/ns/spaceos/0.1/人間API>
SELECT ?url ?g
WHERE {
    GRAPH <http://localhost:3030/memory/data/テスト>  {
      ?room :場所 :ここ .
      ?room :在室 ?p .
      ?c :主人 ?p .
      ?c ha:テキストメッセージ ?url .
    }
}
"""
        results = sa.get(query)
        for result in results["results"]["bindings"]:
            print(result["url"]["value"])
            #print(result["g"]["value"])

        print "TestGet2"
        pass

    def testUpdate(self):
        sa = RdfUploader(self.base+"memory/update")
        query = """
PREFIX : <http://bizar.aitc.jp/ns/spaceos/0.1/> 
PREFIX ha: <http://bizar.aitc.jp/ns/spaceos/0.1/人間API>
INSERT {
    GRAPH <http://localhost:3030/memory/data/テスト>  {
  _:p01
    :最終認識    "2015-07-11T10:55:20.2+09:00"    ;
    .
  _:c01 
       :主人    _:p01    ;
    :電話番号    "012345678"    ;
    :種別    :携帯電話    ;
    ha:テキストメッセージ    "http://192.168.0.2/51355/ha/message/send" ;
    .
    ?room :在室 _:p01 .
    }
}
WHERE {
    GRAPH <http://localhost:3030/memory/data/テスト>  {
      ?room :場所 :ここ .
      }
}
"""
        r = sa.update_data(query)
        print r.text
        print r.status_code
        print "TestUpdate"
        self.testGet2()
        pass

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()