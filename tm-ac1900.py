import urllib2
import urllib
import re
import smtplib
import email
from email.mime.text import MIMEText

sender = 'xxx@xxx'
smtp_host = 'smtp.exmail.qq.com'
username = 'xxx@xxx'
password = 'xxx'
receiver = 'xxx@xxx'
subject = 'xxx'
content = 'xxx'

def sendmail(receiver, subject, content):
    try:
        msg = MIMEText(content, _subtype='html', _charset='utf-8')
        msg['Subject'] = subject
        msg['To'] = receiver
        msg['From'] = sender
        msg['Date'] = email.Utils.formatdate()

        smtp = smtplib.SMTP(smtp_host)
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()
        smtp.login(username, password)
        smtp.sendmail(sender, receiver, msg.as_string())
        smtp.quit()
    except Exception as e:
        print Exception,":",e

response = urllib2.urlopen('https://www.tanga.com/deals/a9db709e24dc/asus-tm-ac1900-wireless-ac1900-dual-band-gigabit-router-brand-new#close-facebox')
html = response.read()
regex = re.compile("<div class='active-price price-container tanganite-price-container'>.*<span class='price'>(.*)</span>.*<div class='shipping-price-container'>",re.S)
output = regex.findall(html)
# send email to notification
if(output[0] != "SOLD OUT"):
   sendmail(receiver, subject, content)

