#-*- coding: utf-8 -*-
'''
Created on 2015/08/25

@author: m-nakagawa
'''

SPARQL_DEFAULT  = ["application/sparql-results+xml", "application/rdf+xml", "*/*"]
SPARQL_XML      = ["application/sparql-results+xml"]
SPARQL_JSON     = ["application/sparql-results+json", "text/javascript", "application/json"]
RDF_XML         = ["application/rdf+xml"]
RDF_N3          = ["text/rdf+n3", "application/n-triples", "application/turtle", "application/n3", "text/n3", "text/turtle"]
RDF_JSONLD      = ["application/x-json+ld", "application/ld+json"]

#SparqlServer = "http://aitc.dyndns.org/sparql/test/sparql"
SparqlServerTrunk = "http://localhost:3030/test/"
SparqlServer = "http://localhost:3030/test/sparql"
SparqlServerQuery = "http://localhost:3030/test/sparql"
SparqlServerUpdate = "http://localhost:3030/test/update"
SelfServer = "http://localhost:8000"
