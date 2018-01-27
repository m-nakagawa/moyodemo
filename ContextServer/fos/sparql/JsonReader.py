'''
Created on 2015/08/04

@author: m-nakagawa
'''
import json5

class JsonReader(object):
    '''
    Read JSON5 format triples
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
if __name__ == '__main__':
    filename = "data/housesample.json"
    f = open(filename)
    #tx = f.read()
    try:
        json_data = json5.load(f)
    except Exception as e:
        print(e)
    f.close()
    reader = JsonReader()
    print("OK")