#-*- coding: utf-8 -*-
'''
Created on 2015/09/03

@author: m-nakagawa
'''





import os.path

import tornado.httpserver
from tornado.options import options, define
from tornado.web import url

#from fos.server.xDataProxy import DataProxy
from fos.server.ExternalService import ExternalService
from fos.server.FosRequestSender import SparqlQueryHandler, FosRequestSender
from fos.server.HttpService import MainPageHandler, \
    FosRequestHandler, TestFormHandler, SparqlQueryTestHandler, \
    SparqlQueryMorphHandler, ServiceTestHandler, GeneratePageHandler
from fos.server.RecordService import RecordService
from fos.server.RecordService2 import RecordService2
from fos.server.StreamService import WebSocketSubscriber, WebSocketRecorder
from fos.server.WebsocketService import DatalinkWebSocket


#from fos.server.DataService import DataService
#import tornado.web
define("port", default = 8000, help =" run on the given port", type = int)
define("url_prefix", default = '/openmasami', help = " root path", type = str)
define("log", default = 'INFO', help = " logging level(DEBUG,INFO..)", type = str)

if __name__ == '__main__':
    tornado.options.parse_command_line()
    options.parse_command_line()
    Url_prefix = options.url_prefix
    
    app = tornado.web.Application(handlers=[
                                            (r'/', MainPageHandler),
                                            (Url_prefix, MainPageHandler),
                                            (Url_prefix+r'/', MainPageHandler),
                                            (Url_prefix+r'/gen/(.+)', GeneratePageHandler),
                                            (Url_prefix+r'/fos/request/(.+)/(.+)', FosRequestHandler),
                                            (Url_prefix+r"/content/(.*)", tornado.web.StaticFileHandler,
                                              {"path": os.path.join(os.path.dirname(__file__), "contents")}),
                                            url(Url_prefix+r'/fostest', TestFormHandler, dict(title='FOS test'), name='fostest'),
                                            url(Url_prefix+r'/test', SparqlQueryTestHandler, dict(title='Sparql query'), name='directtest'),
                                            url(Url_prefix+r'/morphtest', SparqlQueryMorphHandler, dict(title='Morphed query'), name='morphtest'),
                                            url(Url_prefix+r'/requesttest', FosRequestSender, dict(title='Request'), name='requesttest'),
                                            url(Url_prefix+r'/servicetest', ServiceTestHandler, dict(title='Service'), name='servicetest'),
                                            url(Url_prefix+r'/request', SparqlQueryHandler, name='request'),
                                            url(Url_prefix+r'/service/(.+)', ExternalService, name='service'),
                                            url(Url_prefix+r'/record/(.+)', RecordService2, name='record'),
                                            url(Url_prefix+r'/record2/(.+)', RecordService, name='record2'),
                                            #url(Url_prefix+r'/record/(.+)', DataProxy, name='record'),
                                            #url(Url_prefix+r'/data/(.+)', DataService, name='data'),
                                            #url(Url_prefix+r'/data/(.+)', RecordService, name='data'),
                                            #url(Url_prefix+r'/link', EchoWebSocket, name='link'),
                                            url(Url_prefix+r'/link', DatalinkWebSocket, name='link'),
                                            url(Url_prefix+r'/stream/ws/subscribe/(.+)', WebSocketSubscriber, name='ws_subscribe'),
                                            url(Url_prefix+r'/stream/ws/record/(.+)', WebSocketRecorder, name='ws_record'),
                                            ],
                                  template_path=os.path.join(os.path.dirname(__file__), "contents"),
                                  static_path = "contents",
                                  debug = True
                                  )
    http_server = tornado.httpserver.HTTPServer(app)
    http_server.listen(options.port)
    
    tornado.ioloop.IOLoop.instance().start()
   
