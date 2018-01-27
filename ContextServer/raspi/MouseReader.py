'''
Created on 2015/09/14

@author: m-nakagawa
'''
class MouseReader(object):
    _Max = 100
    def __init__(self):
        self.ms = open("/dev/input/mouse0", "rb")
        self.cnt = 0
        self.x = MouseReader._Max/2
        self.y = MouseReader._Max/2
        
    def get_data(self):
        r = self.ms.read(3)
        self.cnt += 1
        
        dx = ord(r[1])
        if dx>128:
            dx = dx-256
        dy = ord(r[2])
        if dy>128:
            dy = dy-256
        
        self.x += dx
        if self.x < 0:
            self.x = 0
        if self.x > MouseReader._Max:
            self.x = MouseReader._Max
            
        self.y += dy
        if self.y < 0:
            self.y = 0
        if self.y > MouseReader._Max:
            self.y = MouseReader._Max
        
        return(self.x, self.y)
        
if __name__ == '__main__':
    m = MouseReader()
    while True:
        (x,y) = m.get_data()
        print x, y
        