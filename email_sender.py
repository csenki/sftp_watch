#! python

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

class email_sender:
    email_body=''
    email_to=''
    email_from=''
    email_subj=''
    email_smtp='127.0.0.1'
    def send_email(self) :
       msg = MIMEMultipart()
       msg['From'] =self.email_from
       msg['To'] = self.email_to
       msg['Subject'] = self.email_subj
       # add in the message body
       msg.attach(MIMEText(self.email_body, 'plain'))
 
       #create server
       server = smtplib.SMTP(self.email_smtp)
       # send the message via the server.
       server.sendmail(msg['From'], msg['To'], msg.as_string())
       server.quit()
 
