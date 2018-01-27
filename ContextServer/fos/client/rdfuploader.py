# -*- coding: utf-8 -*-
'''
Created on 2015/04/14

@author: m-nakagawa
'''
import sys
import requests

class RdfUploader(object):
    '''
    classdocs
    '''


    def __init__(self, url):
        '''
        Constructor
        '''
        self.url = url
        self.headers = {'content-type': "text/turtle;charset=utf-8;"}
        
    def file(self, graph, files, length):
        #ファイルアップロードはうまくいかない
        headers = {'content-type': "text/turtle;charset=utf-8;"}
        headers['content-length'] = unicode(length)

        r = requests.post(self.url+"?"+graph, files=files, headers=headers)
        #r = requests.post(self.url, data=files)
        print r.text
        print r.status_code
        
    def graph_select(self,graph):
        if graph is None:
            return u'default'
        else:
            return u'graph='+graph
        return 
        
    # putだと置き換え、postだと追加
    def upload_data(self, data, graph=None, replace=True):
        graph = self.graph_select(graph)
        if replace:
            r = requests.put(self.url+u"?"+graph, data=data, headers=self.headers)
        else:
            r = requests.post(self.url+u"?"+graph, data=data, headers=self.headers)
        #r = requests.post(self.url, data=files)
        return r
        
    def download_data(self, graph=None):
        graph = self.graph_select(graph)
        r = requests.get(self.url+u"?"+graph, data=data, headers=self.headers)
        return r
        
    def update_data(self, data):
        headers = {'content-type': "application/sparql-update;charset=utf-8;"}
        r = requests.post(self.url, data=data, headers=headers)
        #r = requests.post(self.url, data=files)
        return r
        
if __name__ == "__main__":
    #uploader = RdfUploader("http://aitc.dyndns.org/sparql/test/data")
    uploader = RdfUploader("http://localhost:3030/test/data")
    #uploader = RdfUploader("http://172.22.14.203:3030/test/data")
    #filename = "data/mysample10.ttl"
    filename = sys.argv[1]
    data = open(filename, 'rb').read()
    graph = None
    #graph = u"テスト"
    #r = uploader.data(data, graph=None)
    #r = uploader.upload_data(data, graph=u'テスト')
    r = uploader.upload_data(data, graph=graph)
    if r.status_code != 204 and r.status_code != 201 and r.status_code != 200:
        print r.text
        print r.status_code
    
    #r = uploader.download_data(graph=None)
    r = uploader.download_data(graph=graph)
    r.encoding = 'utf-8'
    print unicode(r.text)
    print r.status_code

    
    
    