#coding=utf-8
#import sys, urllib2

'''
req = urllib2.Request("http://www.baidu.com/")
fd = urllib2.urlopen(req)
print fd.geturl()

info = fd.info()
for key, value in info.items():
    print "%s = %s"%(key, value)

while 1:

    data = fd.read()
    if not len(data):
        break
    sys.stdout.write(data)
'''
'''
from xml.dom import minidom, Node


def scanNode(node, level = 0):
    msg = node.__class__.__nme__
    if node.nodeType == Node.ELEMENT_NODE:
        msg += ", tag: " + node.tagName
    print " " * level * 4, msg
    if node.hasChildNodes:
        for child in node.childNodes:
            scanNode(child, level+1)

doc = minidom.parse('sample.xml')
scanNode(doc)

'''
'''
#make a xml var DOM
from xml.dom import minidom, Node

doc = minidom.Document()
doc.appendChild(doc.createComment("Sample xml Doc"))

book = doc.createElement('book')
doc.appendChild(book)

#tittle
tittle1 = doc.createElement('tittle')
tittle1.appendChild(doc.createTextNode('Sample XML Thing 1'))
book.appendChild(tittle1)

tittle2 = doc.createElement('tittle')
#tittle2.appendChild(doc.createTextNode('Sample XML Thing 2'))
book.appendChild(tittle2)

company1 = doc.createElement('company')
company1.appendChild(doc.createTextNode('hewei dongguan'))
tittle2.appendChild(company1)

company2 = doc.createElement('company2')
company2.appendChild(doc.createTextNode('fucking'))
tittle2.appendChild(company2)

#print doc.toprettyxml(indent= '')
print doc.toxml()
'''
'''
from email.MIMEText import MIMEText
from email import Utils

message = u'hello'.encode('utf-8') + u'你好'.encode('utf-8') + u'good night'.encode('utf-8')
msg = MIMEText(message)
msg['To'] = 'qt19911220@qq.com'
msg['From'] = '941903815@qq.com'
msg['Subject'] = 'Test'
msg['Date'] = Utils.formatdate(localtime = 1)
msg['Message-ID'] = Utils.make_msgid()

print msg.as_string()
'''

'''
import smtplib
from email.mime.text import MIMEText
from email import Utils
_user = ".com"
_pwd = ""
_to = ".com"

# 使用MIMEText构造符合smtp协议的header及body
message = u'hello'.encode('utf-8') + u' '.encode('utf-8') + u'good night'.encode('utf-8')
msg = MIMEText(message)
msg["Subject"] = "don't panic"
msg["From"] = _user
msg["To"] = _to
msg['Date'] = Utils.formatdate(localtime = 1)
msg['Message-ID'] = Utils.make_msgid()


s = smtplib.SMTP_SSL("smtp.qq.com", 465)  # 连接smtp邮件服务器,端口默认是25
s.login(_user, _pwd)  # 登陆服务器
s.sendmail(_user, _to, msg.as_string())  # 发送邮件
s.close()
'''

import smtplib
from email.mime.text import MIMEText
_user = "941903815@qq.com"
_pwd  = "qkfcvmtacugdbfic"
_to   = "boy_johnney@163.com"

message = u'hello'.encode('utf-8') + u'你好，这是来自天朝程序员的问候'.encode('utf-8') + u'good night'.encode('utf-8')

msg = MIMEText(message)
msg["Subject"] = u"你好".encode('utf-8')
msg["From"]    = _user
msg["To"]      = _to

try:
    #not ssl port is 25
    s = smtplib.SMTP_SSL("smtp.qq.com", 465)
    if s.ehlo()[0]>= 200 and s.ehlo()[0] <=299:
        print "support TLS"
    #if support starttls
    print s.has_extn('starttls')
    s.starttls()
    s.login(_user, _pwd)
    s.sendmail(_user, _to, msg.as_string())
    s.quit()
    print "Success!"
except smtplib.SMTPException,e:
    print "Falied,%s"%e