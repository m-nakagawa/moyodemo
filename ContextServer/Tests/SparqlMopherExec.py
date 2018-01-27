'''
Created on 2015/02/03
-*- coding: utf-8 -*-
@author: m-nakagawa
'''

import logging
import sys

from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
from antlr4.tree.Tree import TerminalNodeImpl

from fos.sparql.MorpherContext3 import MorpherContext3
#from fos.sparql.MorpherContext2 import MorpherContext2
from fos.sparql.MySparqlParserListener import MySparqlParserListener
from fos.sparql.SparqlLexer import SparqlLexer
from fos.sparql.SparqlParser import SparqlParser
from fos.sparql.fmind import Fmind


#from SparqlMorpher.MorpherContext2 import MorpherContext2
def toFmind(parent_fnode, node):
    if isinstance(node, TerminalNodeImpl):
        parent_fnode.make_child(unicode(node.getText()))
    else:
        name = SparqlParser.ruleNames[node.getRuleIndex()]
        clsname = node.__class__.__name__
        fnode = parent_fnode.make_child("%s(%s)" % (name,clsname))
        for c in node.getChildren():
            toFmind(fnode, c)
 
def main(argv):
    logfmt=('[%(levelname)s]\t%(name)s:%(threadName)-10s'+
            '(%(asctime)s.%(msecs)d) '+
            '%(filename)s:%(lineno)d:%(message)s')
    datefmt='%H:%M:%S'
    logging.basicConfig(level=logging.INFO,
                        format=logfmt,
                        datefmt=datefmt)

    #input = FileStream(argv[1])
    gname = argv[1]
    inputstream = FileStream(gname, encoding='utf-8')
    lexer = SparqlLexer(inputstream)
    stream = CommonTokenStream(lexer)
    parser = SparqlParser(stream)
    #tree = parser.StartRule()
    tree = parser.query()
    fmind = Fmind(gname)
    fnode = fmind.make_right(u"root")
    toFmind(fnode, tree)
    fmind.unfold_all()
    fmind.dump_to_file("l2.mm")
    
    #tree = parser.prologue()
    slicing = True
    morpher = MorpherContext3(slicing=slicing)
    listener = MySparqlParserListener(morpher)
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    logging.info("Output:%s", sys.argv[1])
    print "# ", sys.argv[1]
    
    if not slicing:
        print morpher.get_result()
    else:
        pre, array = morpher.get_result()
        for s in array:
            print "------------------"
            print pre+s
        
    #print "------------------------------"
    #walker.walk(listener, tree)
 


if __name__ == '__main__':
    main(sys.argv)