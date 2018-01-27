'''
Created on 2015/09/01

@author: m-nakagawa
'''
import sys
import urllib


if __name__ == '__main__':
    filename = sys.argv[1]
    if filename == '-':
        data = sys.argv[2]
    else:
        data = open(filename, 'rb').read()
    print urllib.urlencode({'query': data})

