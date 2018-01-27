# -*- coding: utf-8-dos -*-
'''
Created on 2015/08/06

@author: m-nakagawa
'''
#from antlr4 import FileStream, CommonTokenStream, ParseTreeWalker
#from antlr4 import InputStream, CommonTokenStream, ParseTreeWalker
import antlr4
from antlr4.InputStream import InputStream

from MorpherContext3 import MorpherContext3
#from MorpherContext2 import MorpherContext2
from SparqlLexer import SparqlLexer
from SparqlParser import SparqlParser
#from fos.sparql import MySparqlParserListener


from fos.sparql.MySparqlParserListener import MySparqlParserListener
#import antlr4.InputStream
#from antlr4.tree.Tree import TerminalNodeImpl
class SparqlMorpher(object):
    '''
    classdocs
    '''

    @classmethod
    def morph(cls,src,slicing=False):
        #filename = "Test4.sparql"
        #inputstream = antlr4.InputStream.InputStream(src)
        inputstream = InputStream(src)
        lexer = SparqlLexer(inputstream)
        stream = antlr4.CommonTokenStream(lexer)
        parser = SparqlParser(stream)
        #tree = parser.StartRule()
        tree = parser.query()
        #fmind = Fmind(gname)
        #fnode = fmind.make_right(u"root")
        #toFmind(fnode, tree)
        #fmind.unfold_all()
        #fmind.dump_to_file("l.mm")
        
        #tree = parser.prologue()
    
        morpher = MorpherContext3(slicing=slicing)
        listener = MySparqlParserListener(morpher)
        walker = antlr4.ParseTreeWalker()
        walker.walk(listener, tree)
    
        #logging.info("Output:%s", sys.argv[1])
        #print "# ", sys.argv[1]
        return morpher.get_result()

    def __init__(self, params):
        '''
        Constructor
        '''
        
        
if __name__ == '__main__':
    data = u"""
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/> \r
PREFIX ha: <http://bizar.aitc.jp/ns/fos/0.1/人間API>\r
SELECT ?url ?g\r
WHERE {\r
      GRAPH ?g {\r
      ?room :場所 :ここ .\r
      ?room :在室 ?p .\r
      ?c :主人 ?p .\r
      ?c ha:テキストメッセージ ?url .\r
      }\r
}    \r
    """
    data2 = u"""
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>
PREFIX  ha:  <http://bizar.aitc.jp/ns/fos/0.1/人間API/>
SELECT  ?x ?url
WHERE {
  {
    SELECT  ?url
    WHERE  {
      ?room  :場所  :ここ  .
      ?room  :在室  ?p  .
      ?c  :主人  ?p  .
      ?c  ha:テキストメッセージ  ?url  .
    }
  }
  ?a :適当 ?url .
  ?a :種別 ?x .
}
    """
#    print data
    print SparqlMorpher.morph(data)
    