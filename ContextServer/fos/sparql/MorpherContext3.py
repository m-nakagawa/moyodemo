#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

from __future__ import print_function

from antlr4.Token import Token
from antlr4.tree.Tree import TerminalNodeImpl

from IndentControl import IndentControl
from SelectNode import SelectNode
from SparqlParser import SparqlParser
from VariableOrTerm import VariableOrTerm


def get_leaf(ctx):
    '''Get leaf object.
    Args:
        :param ctx:
    Returns:
        (isvar, label)
        isvar: True: var
        label: Source string 
    '''
    if isinstance(ctx, TerminalNodeImpl):
        return (None, ctx.symbol.text)

    if len(ctx.children) != 1:
        raise Exception('BUG')
    
    if isinstance(ctx, SparqlParser.GraphTermContext):
        first_child = ctx.children[0]
        return (False, get_leaf(first_child)[1])
    elif isinstance(ctx, SparqlParser.VarContext):
        first_child = ctx.children[0]
        return (True, get_leaf(first_child)[1])
    else:
        first_child = ctx.children[0]
        return get_leaf(first_child)
    
    

  
        
    
class MorpherContext3(object):
    """
    @classmethod
    def print_content(cls,ctx):
        cr = ctx.getChildren()
        if cr is not None:
            for c in cr:
                print( c.getText())
                #name = SparqlParser.ruleNames[c.getRuleIndex()]
                #print "++++ ", name, ":", c.getText()
    """  
 

    def __init__(self, slicing=False):
        self.select_stack = []
        self.vars = {}
        self.current_select = None
        self.values_clause_vars = {}
        self.indent = 0
        self.first = True
        self.__result = ""
        self.slicing = slicing
        self.sliced_query = []
        self.scion = {}  # 
        self.indent_control = IndentControl()
        self.select_stack_save = []
        self.slice_cnt = 0


    def get_result(self):
        return self.__result
    
    def enter_query(self,ctx):
        self.root_ctx = ctx
        #self.c2s = Ctx2Source(ctx)
        
        """
        cr = ctx.getChildren()
        if cr is not None:
            for c in cr:
                if not isinstance(c, TerminalNodeImpl):
                    name = SparqlParser.ruleNames[c.getRuleIndex()]
                    if name != u'selectQuery':
                        print(c.getText())
                    #print "++++ ", name, ":", c.getText()
                else:
                    print(c.getText())
        """
        pass

    def exit_query(self,ctx):
        self.__result = self.gen_source(ctx)
        
    def enter_select(self, ctx, construct=False):
        select = SelectNode(construct)
        self.ctx = ctx
        self.select_stack.append(self.current_select)
        self.current_select = select


    def exit_select(self):
        #MopherContext.print_content(self.ctx)
        #self.current_select.print_vars()

        self.current_select.finish()
        #self.current_select.print_vars() #\\
        '''
        cr = self.ctx.getChildren()
        if cr is not None:
            for c in cr:
                name = SparqlParser.ruleNames[c.getRuleIndex()]
                if name != u'selectQuery':
                    print(name+":", Ctx2Source.doit(c))
                    #print(name+":\n", c.getText())

        '''
        self.select_stack_save = self.current_select 
        self.current_select = self.select_stack.pop()
        
    def exit_selectClause(self,ctx):
        # Selectの対象が'*'かどうか
        for c in ctx.getChildren():
            if isinstance(c, TerminalNodeImpl) and c.symbol.text == u'*':
                self.current_select.set_all_result()
        
    def set_variable(self,v):
        #v = VariableOrTerm(ctx)
        self.vars[v.get_string()] = v
        if self.current_select is not None:
            self.current_select.set_variable(v)
        else:
            self.values_clause_vars[v.get_symbol()] = v

    def enter_select_variables(self, ctx):
        (isvar, label) = get_leaf(ctx)
        leaf = VariableOrTerm.get(self, isvar, label)
        self.current_select.set_select_variable(leaf)

    def enter_where_clause(self,ctx):
        self.current_select.enter_where_clause()
        self.add_scion(ctx, self.current_select)

    def enter_values_clause(self,ctx):
        if self.current_select is not None:
            self.current_select.enter_values_clause()

    def set_subject(self,ctx):
        (isvar, label) = get_leaf(ctx)
        leaf = VariableOrTerm.get(self, isvar, label)
        #leaf.set_subject()
        self.subject = leaf
        #print( "Subject:", label)
        
    def set_predicate(self,ctx):
        (isvar, label) = get_leaf(ctx)
        leaf = VariableOrTerm.get(self, isvar, label)
        self.predicate = leaf
        leaf.set_predicate(self.current_select, self.subject)
        #print( "Predicate:", label)
        
    def set_object(self,ctx):
        (isvar, label) = get_leaf(ctx)
        leaf = VariableOrTerm.get(self, isvar, label)
        leaf.set_object(self.current_select, self.subject, self.predicate)

        
        
    def add_scion(self, ctx, obj):
        self.scion[ctx] = obj
    
    def gen_source(self,ctx):
        '''
        Generate source code for this context.
        Returns:
            Source code as a string.
        '''
        self.pre = u'PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>'
        self.pre += u"\n"         
        self.pre += u'PREFIX acc: <http://bizar.aitc.jp/ns/fos/0.1/accesscontrol/>'
        if not self.slicing:
            return self.pre + self.gen_source_do(ctx)
        else:
            s =  self.gen_source_do(ctx)
            self.sliced_query.append(s)
            ret = (self.pre, self.sliced_query) 
            return ret

    def gen_source_do(self, ctx):
        if isinstance(ctx, TerminalNodeImpl):
            if ctx.symbol.type == Token.EOF:
                return ""
            ret = self.indent_control.get_spacer(ctx.symbol.line, ctx.symbol.column)
            ret += ctx.symbol.text
        else:
            scion = self.scion.get(ctx)
            
            if scion is not None:
                ret = self.indent_control.get_spacer(ctx.start.line, ctx.start.column)
                ret += scion.pre(self.indent_control, ctx.start.column)
                ignore_cnt = 1
            else:
                ret = ""
                ignore_cnt = 0
                
            for cr in ctx.getChildren():
                if ignore_cnt == 0:
                    s = self.gen_source_do(cr)
                    ret += s
                else:
                    ignore_cnt -= 1
        
            if scion is not None:
                ret += scion.post(self.indent_control)

        if isinstance(ctx, SparqlParser.SubSelectContext) and self.slicing:
            self.sliced_query.append(ret)
            self.slice_cnt += 1
            ret = "$$$%d$$$" %(self.slice_cnt)
        elif isinstance(ctx, SparqlParser.PrologueContext) and self.slicing:
            self.pre += ret
            ret = ""

        return ret
