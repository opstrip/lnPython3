#!/usr/bin/env python
# -*- coding: utf-8 -*-
# -*- coding: gbk -*-
"""
@Date: Tue Jun 12 14:43:58 2018
@Author: Jeff <370610810@qq.com>
@Link: 
@PythonVersion: v2.7.10
@Filename: sendmail.py
"""
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.utils import parseaddr, formataddr
import smtplib
import os.path
import codecs
import datetime,time


def _format_addr(s):
    """格式化邮件地址"""
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
    
class sendmail:
    """使用Python以指定邮箱发送邮件"""
    mail_host = 'smtp.163.com'
    mail_from = 'lemoncn2014@163.com'
    mail_user = 'lemoncn2014'
    mail_passwd = 'jgyMJU&,ki8'
    msg = MIMEMultipart()
    def __init__(self,mailContent,mailTo,getTitle,fileList):
        """使用email函数库构造email内容"""
        # 对邮件内容、收件人、抄送人、标题、附件执行初始化
        self.mail_content = mailContent
        self.mail_to = mailTo
        self.mail_cc = '370610810@qq.com'
        self.get_title = getTitle
        self.file = fileList
        
        """开始构造email
        ---构建带附件的邮件实例"""
        # 构建邮件头信息
        sendmail.msg['From'] = _format_addr('<%s>' % sendmail.mail_from)
        sendmail.msg['To'] = _format_addr('<%s>' % self.mail_to)
        sendmail.msg['Cc'] = _format_addr('<%s>' % self.mail_cc)
        sendmail.msg['Subject'] = Header(self.get_title).encode('utf8')
        # sendmail.msg['Date'] = time.strftime('%a, %Y-%m-%d %H:%M:%S %z')
        # 构建邮件正文
        sendmail.msg.attach(self.mail_content)
        # 如果附件列表不为空，则构建邮件附件
        if self.file:
            print('Attachment(s) as follow：%s' % format(self.file))
            #使用with安全地打开文件
            with open(self.file, 'rb') as i:
                atta = MIMEText(i.read(), 'base64', 'utf8')
                atta["Content-Type"] = 'application/octet-stream'
                atta["Content-Disposition"] = 'attachment; filename="{}"'.format(os.path.basename(self.file))
                sendmail.msg.attach(atta)
        else:
            print('This message has no attachment.')

        # 将图片附加到邮件正文
        with open(self.file, 'rb') as f:
            msgImage = MIMEImage(f.read())
            # 定义图片 ID，在 HTML 文本中引用
            msgImage.add_header('Content-ID', '<image1>')
            sendmail.msg.attach(msgImage)
            
    def send_mail(self):
        try:
            # 来源：http://www.oschina.net/code/snippet_2293291_55062
            # ssl端口为465/994，非ssl协议的smtp端口是25
            smtpObj = smtplib.SMTP_SSL(sendmail.mail_host, 994)
            # debug级别，1为开启；0关闭
            smtpObj.set_debuglevel(1)
            smtpObj.login(sendmail.mail_user, sendmail.mail_passwd)
            smtpObj.sendmail(sendmail.mail_from, [self.mail_to,self.mail_cc], sendmail.msg.as_string())
            print(time.strftime('%a, %Y-%m-%d %H:%M:%S %z'),'sendmail succeed.')
        except Exception as e:
            print(e)
            print(time.strftime('%a, %Y-%m-%d %H:%M:%S %z'),'sendmail failed.')
        finally:
            smtpObj.quit()
            
def main():
    # 指定相应邮件头信息，将以下邮件地址替换为您自己的邮件地址作为接收方。
    mymail = '370610810@qq.com'
    title = '[通知]这里是标题'.decode('utf8')
    # 指定邮件正文
    # 定义邮件html格式正文
    f = """
    <html><title>这里是正文标题</title><body>
    <p>段落一</p>
    <p>段落二</p>
    <center><a href="http://opstrip.com/" target="_blank" alt="OPSTRIP.COM"><img src="cid:image1" height="80px" width="80px" alt="关注二维码" /></a></center>
    <p>段落三</p>
    <p><font size="-2" color="gray">段落四</font></p>
    <hr>
    <p>段落五</p>
    </body></html>
    """
    # 生成邮件正文
    content = MIMEText(f,'html','utf-8')
    # 创建邮件附件
    file = "/Python2/qrcode.png"
    # file = "C:/Users/admin/Downloads/localhost.%s.log" % ((datetime.datetime.now() - datetime.timedelta(days=1)).strftime("%Y-%m-%d"))
    # 调用sendmail类发送邮件
    sdm = sendmail(content,mymail,title,file)
    sdm.send_mail()

if __name__ == '__main__':
    main()
