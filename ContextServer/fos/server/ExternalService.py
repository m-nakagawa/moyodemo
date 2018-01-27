#-*- coding: utf-8 -*-
'''
Created on 2015/09/01

@author: m-nakagawa
'''
from tornado.log import app_log
import tornado.web

import smtplib
from email.mime.text import MIMEText




def _mail_func(req, command, param):
    #fromaddr = "crypticmemo@ybb.ne.jp"
    fromaddr = "m-nakagawa@nssys.co.jp"
    #toaddr = "m-nakagawa@nssys.co.jp"
    #toaddr = "masami65535.ezweb.ne.jp"
    toaddr = "mn32768@ybb.ne.jp"

    app_log.info("MAIL:%s:%s", toaddr, '/'.join(command))
    msg = MIMEText("メールが送れることのテスト")
    msg['Subject'] = '助けて'
    msg['From'] = fromaddr
    msg['To'] = toaddr

    s = smtplib.SMTP()
    s.connect()
    s.sendmail(fromaddr, [toaddr], msg.as_string())
    s.close()
    return "Sent"


def _printlog_func(req, command, param):
    app_log.info("LOG:%s", '/'.join(command))
    return ""


_Services = {
             'mail': _mail_func,
             'printlog': _printlog_func,
             }

def _web_func(command,params):
    pass

class ExternalService(tornado.web.RequestHandler):
    '''
    classdocs
    '''

    @tornado.web.asynchronous
    @tornado.gen.engine
    def get(self, *args, **kwargs):
        yield self.common(args, kwargs)

    @tornado.web.asynchronous
    @tornado.gen.engine
    def put(self, *args, **kwargs):
        yield self.common(args, kwargs)

    @tornado.web.asynchronous
    @tornado.gen.engine
    def post(self, *args, **kwargs):
        yield self.common(args, kwargs)
    
    @tornado.gen.coroutine    
    def common(self, args, kwargs):
        app_log.debug(args[0])
        command = args[0].split("/")
        func = _Services.get(command[0])
        if func is None:
            raise tornado.web.HTTPError(404)
        
        ret = func(self, command, self.get_argument(u'params', None))
        if ret is not None:
            self.write(ret)
        self.finish()
    
