from flask_mail import smtplib
from email.mime.text import MIMEText
import time
class mailsender:
    def __init__(self, g_tos, g_subjects, g_contents):
        self.G_tos = g_tos
        self.G_subjects = g_subjects
        self.G_contents = g_contents
    def sendmail(self):
        mail_user='mail_user'
        mail_pass='gxgzznpxijaxzlsj'
        mail_postfix="gmail.com"
        me="Monitoring Alarm"+"<"+mail_user+">"
        msg = MIMEText(self.G_contents,_subtype='plain',_charset='utf8')
        msg['Subject'] = self.G_subjects
        msg['From'] = me
        msg['To'] = ";".join(self.G_tos)
        try:
            server = smtplib.SMTP('smtp.gmail.com:587')
            server.ehlo()
            server.starttls()
            server.ehlo()
            server.login(mail_user,mail_pass)
            print msg.as_string()
            server.sendmail(me, self.G_tos, msg.as_string())
            server.quit()
            return 'True'
        except Exception, e:
            print str(e)
            return 'False'
