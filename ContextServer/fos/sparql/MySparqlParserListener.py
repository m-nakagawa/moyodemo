#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

# Generated from java-escape by ANTLR 4.4
#from antlr4 import *
from SparqlParserListener import SparqlParserListener

# This class defines a complete listener for a parse tree produced by SparqlParser.
class MySparqlParserListener(SparqlParserListener):

    def __init__(self, morpher):
        self.morpher = morpher

 
    # Enter a parse tree produced by SparqlParser#var.
    def enterVar(self, ctx):
        pass

    # Exit a parse tree produced by SparqlParser#var.
    def exitVar(self, ctx):
        #MN
        #print "Exit Var:", type(ctx)
        #cr = ctx.getChildren()
        #if cr is not None:
        #    for c in cr:
        #        s = c.getSymbol()
        #        print "---- ", c.getText(), s.text[1:]
        #        ctx.get_masami_root().set_variable(c)
        #self.morpher.set_variable(ctx)
        pass


 
    # Enter a parse tree produced by SparqlParser#selectQuery.
    def enterSelectQuery(self, ctx):
        #MN
        #print "SelectQuery", ctx
        self.morpher.enter_select(ctx)
        pass

    # Exit a parse tree produced by SparqlParser#selectQuery.
    def exitSelectQuery(self, ctx):
        #MN
        #print "Ex SelectQuery", ctx
        self.morpher.exit_select()
        pass

    # Enter a parse tree produced by SparqlParser#selectClause.
    def enterSelectClause(self, ctx):
        pass

    # Exit a parse tree produced by SparqlParser#selectClause.
    def exitSelectClause(self, ctx):
        self.morpher.exit_selectClause(ctx)

    # Enter a parse tree produced by SparqlParser#constructQuery.
    def enterConstructQuery(self, ctx):
        self.morpher.enter_select(ctx, construct=True)

    # Exit a parse tree produced by SparqlParser#constructQuery.
    def exitConstructQuery(self, ctx):
        self.morpher.exit_select()


    # Enter a parse tree produced by SparqlParser#baseDecl.
    def enterBaseDecl(self, ctx):
        #print "BaseDecl", ctx
        pass

    # Exit a parse tree produced by SparqlParser#baseDecl.
    def exitBaseDecl(self, ctx):
        #print "Ex BaseDecl", ctx
        pass

    # Enter a parse tree produced by SparqlParser#subSelect.
    def enterSubSelect(self, ctx):
        self.morpher.enter_select(ctx)
        pass

    # Exit a parse tree produced by SparqlParser#subSelect.
    def exitSubSelect(self, ctx):
        self.morpher.exit_select()
        pass


    # Enter a parse tree produced by SparqlParser#selectVariables.
    def enterSelectVariables(self, ctx):
        #print "SelectVariables", ctx
        self.morpher.enter_select_variables(ctx)
        pass

    # Exit a parse tree produced by SparqlParser#selectVariables.
    def exitSelectVariables(self, ctx):
        #print "Ex SelectVariables", ctx
        pass


    # Enter a parse tree produced by SparqlParser#whereClause.
    def enterWhereClause(self, ctx):
        self.morpher.enter_where_clause(ctx)


    # Exit a parse tree produced by SparqlParser#whereClause.
    def exitWhereClause(self, ctx):
        pass


    # Enter a parse tree produced by SparqlParser#query.
    # MN ここが根
    def enterQuery(self, ctx):
        self.morpher.enter_query(ctx)

    # Exit a parse tree produced by SparqlParser#query.
    def exitQuery(self, ctx):
        #MN
        #print "Ex Query", ctx
        #cr = ctx.getChildren()
        #if cr is not None:
        #    for c in cr:
        #        print "---- ", c.getText()
        self.morpher.exit_query(ctx)




    # Enter a parse tree produced by SparqlParser#valuesClause.
    def enterValuesClause(self, ctx):
        self.morpher.enter_values_clause(ctx)

    # Exit a parse tree produced by SparqlParser#valuesClause.
    def exitValuesClause(self, ctx):
        pass


# Enter a parse tree produced by SparqlParser#varOrTerm.
# Tripleのs
    def enterVarOrTerm(self, ctx):
        self.morpher.set_subject(ctx)
        

    # Exit a parse tree produced by SparqlParser#varOrTerm.
    def exitVarOrTerm(self, ctx):
        #print "VerOrTerm:", ctx.getText()
        pass

# Enter a parse tree produced by SparqlParser#graphTerm.
    def enterGraphTerm(self, ctx):
        pass

    # Exit a parse tree produced by SparqlParser#graphTerm.
    def exitGraphTerm(self, ctx):
        pass

# Enter a parse tree produced by SparqlParser#verbPath.
    def enterVerbPath(self, ctx):
        self.morpher.set_predicate(ctx)

    # Exit a parse tree produced by SparqlParser#verbPath.
    def exitVerbPath(self, ctx):
        pass

    # Enter a parse tree produced by SparqlParser#verbSimple.
    def enterVerbSimple(self, ctx):
        self.morpher.set_predicate(ctx)

    # Exit a parse tree produced by SparqlParser#verbSimple.
    def exitVerbSimple(self, ctx):
        pass

    def enterObjectPath(self, ctx):
        self.morpher.set_object(ctx)
        pass

    # Exit a parse tree produced by SparqlParser#objectPath.
    def exitObjectPath(self, ctx):
        pass

    # Enter a parse tree produced by SparqlParser#objectListPath.
    def enterObjectListPath(self, ctx):
        pass

    # Exit a parse tree produced by SparqlParser#objectListPath.
    def exitObjectListPath(self, ctx):
        pass


