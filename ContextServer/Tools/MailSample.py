#!/Usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText

class sendGmail:
    username, password = 'm.nakagawa.nss@gmail.com', '32057921'

    def __init__(self, to, sub, body):
        #host, port = 'smtp.gmail.com', 25
        host, port = 'smtp.gmail.com', 465
        #host, port = 'smtp.gmail.com', 587
        msg = MIMEText(body)
        msg['Subject'] = sub
        msg['From'] = self.username
        msg['To'] = to

        smtp = smtplib.SMTP_SSL(host, port)
        smtp.ehlo()
        smtp.login(self.username, self.password)
        smtp.rcpt(to)
        smtp.data(msg.as_string())
        smtp.quit()

if __name__ == '__main__':
    to = 'masami65535@ezweb.ne.jp'
    sub = 'Python smtplib'
    body = 'Hello, Python'
    sendGmail(to, sub, body)
