# -*- coding: utf-8 -*-
'''
Created on 2015/04/13
-*- coding: utf-8 -*-
@author: m-nakagawa
'''

from SPARQLWrapper import SPARQLWrapper, JSON, TURTLE
 
#sparql = SPARQLWrapper("http://dbpedia.org/sparql")
sparql = SPARQLWrapper("http://localhost:3030/memory/sparql")
#sparql.setQuery("""
#    PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#    SELECT ?label
#    WHERE { <http://dbpedia.org/resource/Asturias> rdfs:label ?label }
#""")
sparql.setQuery("""
# 日本語
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/> 
PREFIX ha: <http://bizar.aitc.jp/ns/fos/0.1/人間API>
SELECT ?url
WHERE {
      ?room :場所 :ここ .
      ?room :在室 ?p .
      ?c :主人 ?p .
      ?c ha:テキストメッセージ ?url .
}
""")
#sparql.setQuery("""
## 日本語
#PREFIX : <http://bizar.aitc.jp/ns/spaceos/0.1/> 
#PREFIX ha: <http://bizar.aitc.jp/ns/spaceos/0.1/人間API>
#CONSTRUCT{ ?url :test "abc" .}
#WHERE {
#      ?room :場所 :ここ .
#      ?room :在室 ?p .
#      ?c :主人 ?p .
#      ?c ha:テキストメッセージ ?url .
#}
#""")
sparql.setReturnFormat(JSON)
#sparql.setReturnFormat(TURTLE)
results = sparql.query().convert()
 
for result in results["results"]["bindings"]:
    #print(result["label"]["value"])
    print(result["url"]["value"])
    #print(result[".1"]["value"])

for d in sparql.query():
    print d
    