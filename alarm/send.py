#!/usr/bin/env python

from config import sender,receiver,smtp,username,password
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication
from shoot import shoot

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

if __name__ == "__main__":
    print "test email...",
    send_email("Email send test",
               "this is a example...")
    print "ok"
    print "test send photo...",
    try:
        filename = shoot()
        send_email("Photo","Picture From RaspberryPI.",filename)
    except Exception,e:
        print e
    print "ok"

