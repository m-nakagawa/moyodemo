# -*- coding: utf-8 -*-
'''
Created on 2015/04/14

@author: m-nakagawa
'''

from SPARQLWrapper import SPARQLWrapper #, JSONLD
from SPARQLWrapper.Wrapper import JSONLD, JSON


class SparqlAccess(object):
    def __init__(self, url):
        self.url = url
        self.sparql = SPARQLWrapper(url)
        
    def select(self, query):
        self.sparql.setReturnFormat(JSON)
        self.sparql.setQuery(query)
        return self.sparql.query().convert()
    
    def construct(self, query):
        self.sparql.setReturnFormat(JSONLD)
        self.sparql.setQuery(query)
        return self.sparql.query().convert()
    
    def apply(self, query):
        self.sparql.setReturnFormat(JSONLD)
        self.sparql.method = 'POST'
        self.sparql.setQuery(query)
        return self.sparql.query().convert()
    
    def update(self, query):
        self.sparql.method = 'POST'
        self.sparql.setQuery(query)
        return self.sparql.query()
        