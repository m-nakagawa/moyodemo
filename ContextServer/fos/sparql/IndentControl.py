'''
Created on 2015/02/04

@author: m-nakagawa
'''

class IndentControl(object):
    def __init__(self, indent_unit = u'    '):
        self.current_line = -1
        self.extra_indent = 0
        self.extra_indent_str = ''
        self.indent_unit = indent_unit
        
    def get_spacer(self,line,column):
        if self.current_line == -2:
            self.current_line = line
            return u'\n' + u' '*self.base_indent + self.extra_indent_str
        elif self.current_line != line:
            self.current_line = line
            return u'\n' + u' '*column + self.extra_indent_str
        else:
            return ' '
    
    def get_base_spacer(self):
        return u'\n' + u' '*self.base_indent + self.extra_indent_str

    def new_line(self):
        self.current_line = -1
    
    def enter_extra_indent(self,column):
        '''
        Increase indent and set the next symbol to new line.
        Args:
            column: The next token's indentation. column == -1 indicates to use base_indent as a column.
        '''
        self.extra_indent += 1
        self.extra_indent_str = self.indent_unit*self.extra_indent
        self.current_line = -2
        if column >= 0:
            self.base_indent = column
    
    def exit_extra_indent(self):
        '''
        Decrease indent and set the next symbol to new line
        '''
        self.extra_indent -= 1
        self.extra_indent_str = self.indent_unit*self.extra_indent
        self.current_line = -1
