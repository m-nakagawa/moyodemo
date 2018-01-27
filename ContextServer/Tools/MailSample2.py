# Import smtplib for the actual sending function
import smtplib

# Import the email modules we'll need
from email.mime.text import MIMEText

# Open a plain text file for reading.  For this example, assume that
# the text file contains only ASCII characters.
#fp = open(textfile, 'rb')
# Create a text/plain message
#msg = MIMEText(fp.read())
#fp.close()

fromaddr = "crypticmemo@ybb.ne.jp"
#toaddr = "m-nakagawa@nssys.co.jp"
toaddr = "masami65535.ezweb.ne.jp"

msg = MIMEText("test")

# me == the sender's email address
# you == the recipient's email address
msg['Subject'] = 'Testing'
msg['From'] = fromaddr
msg['To'] = toaddr

# Send the message via our own SMTP server, but don't include the
# envelope header.
s = smtplib.SMTP()
s.connect()
s.sendmail(fromaddr, [toaddr], msg.as_string())
s.close()
