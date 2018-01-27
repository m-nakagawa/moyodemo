'''
Created on 2015/09/01

@author: m-nakagawa
'''
import sys
import urllib


if __name__ == '__main__':
    filename = sys.argv[1]
    data = open(filename, 'rb').read()
    print urllib.unquote(data)
    
