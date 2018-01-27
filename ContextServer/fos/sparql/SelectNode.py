#!/usr/bin/env python
# -*- coding: utf-8-unix -*-

#from morphercontext2 import Scion
from Scion import Scion
from io import StringIO
from VariableOrTerm import VariableOrTerm

class SelectNode(Scion):
    
    def __init__(self, construct):
        self.result_vars = {}
        self.select_vars = {}
        self.where_vars = {}
        self.values_clause_vars = {}
        self.all_vars = {}
        
        self.filter_symbols= []
        self.filter_included = {}

        self.current = self.select_vars
        self.all_result = False # True: SELECT *
        
        self.construct = construct
        
    def finish(self):
        pass

    def set_variable(self, variable):
        self.current[variable.get_string()] = variable

    # SelectClause 縺ｫ'*'縺悟性縺ｾ繧後※縺�繧�
    def set_all_result(self):
        self.all_result = True
        
    #def enter_select_variables(self):
    #    self.current = self.select_vars
    def set_select_variable(self, var):
        self.select_vars[var.get_string()] = var

    def enter_where_clause(self):
        self.current = self.where_vars
        
    def enter_values_clause(self):
        self.current = self.values_clause_vars
        
    def print_vars(self):
        print "SelectVars:",",".join(list(self.select_vars.keys()))
        print "WhereVars:",",".join(list(self.where_vars.keys()))
        print "ValuesVars:",",".join(list(self.values_clause_vars.keys()))

    
    def pre(self,indent_control,column):
        '''
        Generate extra statements before the target block.
        :param indent_control:
        '''
        indent_control.enter_extra_indent(column)
        ret = 'WHERE {'
        return ret

    def post(self,indent_control):
        self.gen_prepare()
        ret = self.gen_optionals(indent_control)
        ret += self.gen_filters(indent_control)
        indent_control.exit_extra_indent()
        ret += indent_control.get_spacer(0,0)+'}'
        return ret
    
    def gen_prepare(self):
        #print "abc"

        for k, v in self.where_vars.items():
            self.all_vars[k] = v
            if self.all_result:
                v.set_result()
        for k in self.select_vars.keys():
            v = self.all_vars.get(k)
            if v is not None:
                v.set_result()
        for k in self.values_clause_vars.keys():
            v = self.all_vars.get(k)
            if v is not None:
                v.set_values_def()
                if self.all_result:
                    v.set_result()

    def add_filter(self,var):
        #if not var.is_var():
        #    return
        
        if self.filter_included.get(var) is None:
            self.filter_symbols.append(var)
            self.filter_included[var] = True
    
    def generate_options1(self, var):
        ret = []
        if var.is_subject():
            ret.append(var.get_string()+u' rdf:type/acc:ctrl '+' '+var.get_acc_name()+u'.')
                        
        self.add_filter(var)

        return ret
    
    def add_options_str(self,s):
        return u'OPTIONAL{' + s + u'}'
    
    def generate_options2(self, var):
        ret = []

        if var.is_object():
            s, p = var.get_subject_predicate(self)
            hide = var.get_hide_symbol()
            if s.is_var():
                temp = VariableOrTerm.get_temp_label()
                r = s.get_string()+u' rdf:type/acc:ctrl ' + temp + u'. '
                r += temp + ' '+ p.get_string()+' ' + hide + u'2 .'
                temp2 = VariableOrTerm.get_temp_label()
                r2 = s.get_string()+u' acc:ctrl ' + temp2 + u'. '
                r2 += temp2 + ' ' + p.get_string()+' '+ hide + u'1 .'
            else:
                r = s.get_string()+u' rdf:type/acc:ctrl/'+p.get_string()+' '+hide+u'2 .'
                r2 = s.get_string()+u' rdf:type/acc:ctrl/'+p.get_string()+' '+hide+u'1 .'
            #ret.append(temp+u' '+p.get_string()+' '+var.get_hide_symbol()+u'.')
            ret.append(self.add_options_str(r))
            ret.append(self.add_options_str(r2))
            self.add_filter(var)
        
        #if var.is_predicate():
        #    ret.append(u'acc:hide '+var.get_string()+' '+var.get_hide_symbol()+u'.')
        #    self.add_filter(var)
        
        r = var.get_string()+' acc:level '+var.get_level_symbol()+u'.'
        ret.append(self.add_options_str(r))
        self.add_filter(var)

        return ret
    
    def generate_filters(self):
        ret = []
        
        for var in self.filter_symbols:
            if var.is_result():
                level = u'2'
            else:
                level = u'3'
            
            fv = []
            fv.append(var.get_level_symbol())  #// type 1
            if var.is_object():
                hide = var.get_hide_symbol()
                fv.append(hide+u'1')
                fv.append(hide+u'2')
            s = u'(coalesce(' + ' ,'.join(fv) + u', 1) < ' + level + u')'
            ret.append(s)

        return ret

    
    def gen_optionals(self,indent_control):
        with StringIO() as builder:
            indent_control.new_line()
            #builder.write(indent_control.get_base_spacer() + u'OPTIONAL {')
            #indent_control.enter_extra_indent(-1)
            #for v in self.all_vars.values():
            #    os = self.generate_options1(v)
            #    for o in os:
            #        builder.write(indent_control.get_base_spacer()+u'OPTIONAL {')
            #        builder.write(o)
            #        builder.write(u'}')
            for v in self.all_vars.values():
                os = self.generate_options2(v)
                for o in os:
                    builder.write(indent_control.get_base_spacer())
                    builder.write(o)


            #builder.write(indent_control.get_base_spacer()+ u"SelectVars:" + ",".join(list(self.select_vars.keys())))
            #builder.write(indent_control.get_base_spacer()+ u"WhereVars:" + ",".join(list(self.where_vars.keys())))
            #builder.write(indent_control.get_base_spacer()+ u"ValueVars:" + ",".join(list(self.values_clause_vars.keys())))

            #indent_control.exit_extra_indent()
            #builder.write(indent_control.get_base_spacer() + u'}')
            return builder.getvalue()


        #for v in self.where_vars.keys():
        #    if not v.is_predicate():
        #        ret += 
    
    def gen_filters(self,indent_control):
        filters = self.generate_filters()
        if len(filters) != 0:
            with StringIO() as builder:
                indent_control.new_line()
                builder.write(indent_control.get_base_spacer() + u'FILTER (')
                indent_control.enter_extra_indent(-1)

                last = filters.pop()
                for fl in filters:
                    builder.write(indent_control.get_base_spacer()+u'(')
                    builder.write(fl)
                    builder.write(u") &&")
                builder.write(indent_control.get_base_spacer()+u'(')
                builder.write(last)
                builder.write(u")")
            
                indent_control.exit_extra_indent()
                builder.write(indent_control.get_base_spacer() + u')')
                return builder.getvalue()
        else:
            return ""