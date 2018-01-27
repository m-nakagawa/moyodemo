#!/usr/bin/env python
# -*- coding: utf-8 -*-


class VariableOrTerm(object):
    index = {}
    cnt = 0
    temp_cnt = 0
    graph_term_index = {}
    
    @classmethod
    def get_temp_label(cls):
        cls.temp_cnt += 1
        return u'?temp_'+str(cls.temp_cnt)   #衝突チェックはしていない
    
    @classmethod
    def get(cls, morpher, isvar, name):
        #print "GET;", name
        if isvar:
            key = '?'+name[1:]
        else:
            key = name
        obj = cls.index.get(key)
        if obj is None:
            obj = VariableOrTerm(isvar,name)
            
        morpher.set_variable(obj)
        return obj
    
    def __init__(self,isvar,name):
        VariableOrTerm.cnt += 1
        self.__isvar = isvar # True: 変数
        if isvar:
            self.text = name[1:]
            self.name = '?'+self.text
            
        else:
            self.name = name
            self.text = '__'+str(VariableOrTerm.cnt)
            #self.text = '__'+name
            VariableOrTerm.graph_term_index[VariableOrTerm.cnt] = self
            
        self.s_p_map = {}   # このオブジェクトがobjectだったときs_p_map[select] = (subject,predicate) いまのところ1個だけ設定できる
        self.p_map = {}     # このオブジェクトがsubjectだったときp_map[select] = subject　いまのところ1個だけ設定できる
        VariableOrTerm.index[self.name] = self
        self.__isresult = False   # True:SELECTの返り値として設定
        self.__issubject = False   # True:SPOのSとして参照
        self.__ispredicate = False
        self.__isobject = False   # True: SPOのOとして参照
        
    def get_string(self):
        return self.name
    
    def get_hide_symbol(self):
        # TODO 重複排除
        return u'?'+self.text+u'_hide'
    
    def get_level_symbol(self):
        # TODO 重複排除
        return u'?'+self.text+u'_level'
    
    def get_acc_name(self):
        return u'?'+self.text+u'_acc'
    
    def is_var(self):
        return self.__isvar

    def set_result(self):
        self.__isresult = True
        
    def is_result(self):
        return self.__isresult
    
    def set_subject(self):
        self.__issubject = True
    
    def is_subject(self):
        return self.__issubject
    
    def is_predicate(self):
        return self.__ispredicate

    def is_object(self):
        return self.__isobject

    def set_predicate(self, select, subject):
        self.p_map[select] = subject
        self.__ispredicate = True
        
    def set_object(self, select, subject, predicate):
        self.s_p_map[select] = (subject, predicate)
        subject.set_subject()
        self.__isobject = True
    
    def set_values_def(self):
        # メソッドの目的わからない
        pass
    
    
    def get_subject_predicate(self, select):
        return self.s_p_map.get(select)

    def get_subject(self, select):
        return self.p_map.get(select)
    
    