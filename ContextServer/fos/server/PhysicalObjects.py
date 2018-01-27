#-*- coding: utf-8 -*-
'''
Created on 2015/09/01

@author: m-nakagawa
'''
import json
import time

from tornado.log import app_log
import tornado.web

from fos.client.Handle import Handle

_Unknown = "unknown"
_Ready = "ready"
_Disconnect = "disconnect"

_ScanAllPhisicalClasses =u"""
PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>
SELECT  ?s ?p ?o
WHERE {
  ?s     rdfs:type    rdfs:class .
  ?s     rdf:subClassOf  :測定値 .
  ?s     ?p    ?o .
}
""" 

_ScanAllSensors = u"""
PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>
SELECT  ?s ?p ?o
WHERE {
  ?clss  rdf:subClassOf  :測定値 .
  ?s     rdf:type     ?clss  .
  ?s     ?p    ?o .
}
"""

_ScanAllActuators = u"""
PREFIX  rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
PREFIX  rdfs:  <http://www.w3.org/2000/01/rdf-schema#>
PREFIX : <http://bizar.aitc.jp/ns/fos/0.1/>
SELECT  ?s ?p ?o
WHERE {
  ?clss  rdf:subClassOf  :制御値 .
  ?s     rdf:type     ?clss  .
  ?s     ?p    ?o .
}
"""

_PhysicalObjects = {}

class Value(object):
    def __init__(self, idfr):
        self.idfr = idfr
        self.value = None
        if _PhysicalObjects.get(idfr) is None:
            _PhysicalObjects[idfr] = self
        else:
            app_log.error("Physical object idfr duplicated2:%s"%(self.idfr))

    def get_idfr(self):
        return self.idfr
         
    def get_value(self):
        return self.value
    
    def set_value(self, value):
        self.value = value
        
    def to_str(self):
        return "%s:%s"%(self.idfr, self.value)
        
        
        
_Time = u"http://bizar.aitc.jp/ns/fos/0.1/時刻"
_Type = u"http://www.w3.org/1999/02/22-rdf-syntax-ns#type"
_Value = u"http://bizar.aitc.jp/ns/fos/0.1/値"

class Sensor(object):
    def __init__(self, idfr):
        self.idfr = idfr
        self.state = _Disconnect
        self.duplicate = 0
        self.values = {}
        self.time = None
        self.type = None
        if _PhysicalObjects.get(idfr) is None:
            _PhysicalObjects[idfr] = self
        else:
            app_log.error("Physical object idfr duplicated:%s"%(self.idfr))
   
    def get_idfr(self):
        return self.idfr
    
    def set_values(self, tm, values):
        for k, v in values.items():
            o = self.values.get(k)
            if o is None:
                app_log.debug("Physical object predicate does not exist:%s:%s"%(k, self.idfr) )
                continue
            o.set_value(v)
        t = self.values.get(_Time)
        if t is not None:
            t.set_value(tm)
        else:
            app_log.debug("Physical object predicate does not exist:時刻:%s"%(self.idfr) )
    
    def get_values(self):
        return self.values
    
    def set_scalar_value(self, tm, value):
        vo = self.values.get(_Value)
        if vo is not None:
            vo.set_value(value)
            to = self.values.get(_Time)
            to.set_value(tm)
    
    def get_scalar_value(self):
        vo = self.values.get(_Value)
        if vo is not None:
            return vo.get_value()
        else:
            return None
        
    def add_value(self, key, idfr):
        if self.values.get(key) is None:
            self.values[key] = Value(idfr)
        else:
            self.set_duplicate()
        
    def set_ready(self):
        self.state = _Ready
    
    def set_disconnect(self):
        self.state = _Disconnect
        
    def get_state(self):
        return self.state
    
    def set_type(self,ty):
        self.type = ty
        
    def get_type(self):
        return self.type
    
    def set_duplicate(self):
        self.duplicate += 1
        
    def get_duplicate(self):
        return self.duplicate

    def to_str(self):
        s = "%s:%s\n"%(self.__class__.__name__,self.idfr)
        s += "  type: %s\n" % (self.type)
        for k, v in self.values.items():
            s += "  %s: %s\n" % (k, v.to_str())
        return s

class Actuator(Sensor):
    '''
    Actuator.
    value: requested target value
    
    '''
    def __init__(self, idfr):
        Sensor.__init__(self, idfr)
        self.accept_time = None
        
    def accepted(self, tm):
        self.accept_time = tm


def gen_sensor(idfr):
    return Sensor(idfr)

def gen_actuator(idfr):
    return Actuator(idfr)

def generate_physical_objects(handle, query, gen_func):
    ret = handle.select(query)
    for r in ret[u'results'][u'bindings']:
        idfr = r[u's']['value']
        if r[u's']['type'] != u'uri':
            app_log.error("Physical object idfr is not a uri:%s"%(idfr) )
            continue
        po = _PhysicalObjects.get(idfr)
        if po is None:
            po = gen_func(idfr)
            
        p = r[u'p']['value']
        if r[u'p']['type'] != u'uri':
            app_log.error("Physical object predicate is not a uri:%s"%(idfr) )
            continue
        o = r[u'o']['value']
        if r[u'o']['type'] != u'uri':
            app_log.error("Physical object predicate is not a uri:%s"%(idfr) )
            continue
        
        if p != _Type:
            po.add_value(p, o)
        else:
            po.set_type(o)    

    
def refresh_all_sensors():
    handle = Handle.getHandle(direct=True)
    
    generate_physical_objects(handle, _ScanAllSensors, gen_sensor)
    generate_physical_objects(handle, _ScanAllActuators, gen_actuator)

def get_physical_object(idfr):
    return _PhysicalObjects.get(idfr)


if __name__ == '__main__':
    refresh_all_sensors()
    for k, o in _PhysicalObjects.items():
        print o.to_str()
        if isinstance(o, Sensor):
            last = o
            
    print "-------"
    last.set_scalar_value(time.time(),123)
    print last.to_str()
    print last.get_scalar_value()
    