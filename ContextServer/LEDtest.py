#-*- coding: utf-8 -*
'''
Created on 2018/01/27

@author: m-nakagawa

'''

import sys
import RPi.GPIO as GPIO

_port = {1:18, 2:23}

if __name__ == '__main__':
    #print u'‚Ä‚·‚Æ'
    #print urllib.quote(u'‚Ä‚·‚Æ'.encode('utf-8'))
    #print urllib.quote(_Base)
    #exit(1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(18,GPIO.OUT)
    GPIO.setup(23,GPIO.OUT)

    print sys.argv
    exit(1)
    
    GPIO.output(_port[self.num], True)
    GPIO.output(_port[self.num], False)
