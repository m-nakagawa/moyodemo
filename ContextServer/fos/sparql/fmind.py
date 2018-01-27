# -*- coding: utf-8-*-

from xml.etree.ElementTree import Element, SubElement, Comment, tostring
from xml.etree import ElementTree
from xml.dom import minidom
import codecs


def to_xml_indent(elem, indent="   "):
    s = ElementTree.tostring(elem, encoding='utf-8', method='xml')
    s = s.decode('utf-8')
    dom = minidom.parseString(s.encode('utf-8'))
    return dom.toprettyxml(indent=indent)


class FNode(object):
    idcnt = 123
    
    def __init__(self,parent,name,flag=None):
        self.parent = parent
        self.children = []
        self.icons = []
        self.name = name
        self.right = False
        self.left = False

        self.id = FNode.idcnt
        FNode.idcnt += 1

        self.folded = True
        if parent is None:
            self.folded = False

        if flag == 'LEFT':
            self.left = True
        elif flag == 'RIGHT':
            self.right = True

    def make_child(self, name, flag=None):
        n = FNode(self, name, flag=flag)
        self.children.append(n)
        return n

    def unfold(self):
        self.folded = False
        
    def fold(self):
        self.folded = True
        
    def unfold_all(self):
        self.unfold()
        for c in self.children:
            c.unfold_all()

    def get_parent(self):
        return self.parent

    def get_name(self):
        return self.name

    def set_name(self,name):
        self.name = name

    def set_icon(self,icon):
        self.icons.append(icon)

    def gen_xml(self,parent):
        me = SubElement(parent,'node')
        me.set('TEXT',self.name)
        me.set('ID', 'ID_'+str(self.id))
        #me.set('CREATED',  '54321')
        #me.set('MODIFIED', '54321')
        if self.left:
            me.set('POSITION', 'left')
        elif self.right:
            me.set('POSITION', 'right')

        if len(self.children) != 0 and self.folded:
            me.set('FOLDED', 'true')

        for i in self.icons:
            ie = SubElement(me,'icon')
            ie.set('BUILTIN', i)

        for c in self.children:
            c.gen_xml(me)
            

class Fmind(object):
    def __init__(self,name):
        self.root = FNode(None,name)

    def get_root(self):
        return self.root

    def make_right(self,name):
        return self.root.make_child(name, flag='RIGHT')

    def make_left(self,name):
        return self.root.make_child(name, flag='LEFT')

    def to_xml(self,indent = "    "):
        top = Element('map')
        top.set('version', '1.0.1')
        top.append(Comment(u'FreeMindフォーマットです'))
        self.root.gen_xml(top)
        return to_xml_indent(top,indent=indent)

    def dump_to_file(self, filename, indent="    "):
        f = codecs.open(filename, 'w', 'utf-8')
        f.write(self.to_xml(indent=indent))
        f.close()


    def unfold_all(self):
        self.root.unfold_all()

if __name__ == '__main__':
    f = Fmind('AAA')
    r = f.make_right('BBB')
    r2 = f.make_right('CCC')
    rr1= r.make_child('123')
    rr1.set_icon('full-1')
    rr2= r.make_child('あいう')
    rr2.set_icon('full-2')
    rr2.set_icon('full-3')
    l = f.make_left('DDD')
#<icon BUILTIN="button_cancel"/> ×
#<icon BUILTIN="help"/> ?
#<icon BUILTIN="button_ok"/> チェック
    
    f.dump_to_file('l.mm')
