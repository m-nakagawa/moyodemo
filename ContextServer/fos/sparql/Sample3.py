'''
Created on 2015/02/03
-*- coding: utf-8 -*-
@author: m-nakagawa
'''

import sys

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker

from SparqlLexer import SparqlLexer
from SparqlParser import SparqlParser
from fos.sparql.MorpherContext2 import MorpherContext2
from fos.sparql.MySparqlParserListener import MySparqlParserListener


def main(argv):
    #input = FileStream(argv[1])
    inputstream = FileStream(argv[1], encoding='utf-8')
    lexer = SparqlLexer(inputstream)
    stream = CommonTokenStream(lexer)
    parser = SparqlParser(stream)
    #tree = parser.StartRule()
    tree = parser.query()
    #tree = parser.prologue()

    morpher = MorpherContext2()
    listener = MySparqlParserListener(morpher)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    print "# ", sys.argv[1]
    print morpher.get_result()
    #print "------------------------------"
    #walker.walk(listener, tree)
 


if __name__ == '__main__':
    main(sys.argv)