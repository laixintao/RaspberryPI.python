#!/usr/bin/env python

from config import sender,receiver,smtp,username,password
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

msg = MIMEMultipart()

msg['to'] = ','.join(receiver)
msg['from'] = sender

def send_email(subject,
               msghtml,
               *att):
    server = smtplib.SMTP()
    server.connect(smtp)
    server.login(username,password)
    # attach
    msgText = MIMEText(msghtml,'html','utf-8')
    msg.attach(msgText)
    print "email is ready..."
    for each in att:
        tmp = MIMEApplication(open(each,'rb').read())
        tmp.add_header('Content-Disposition', 'attachment', filename=each)
        msg.attach(tmp)
        print each+" has been added to attachment..."
    msg['subject'] = subject
    print "now send the email..."
    server.sendmail(sender,receiver,msg.as_string())
    server.quit()
    print 'successfully send email.'
