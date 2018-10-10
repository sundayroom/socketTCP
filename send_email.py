#coding:utf-8
import smtplib


#设置smtplib使用的参数
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

smptserver='stmp.163.com'
username='18844141433@163.com'
password='qwe123asd'
sender='18844141433@163.com'
receiver=['2216936901@qq.com']
#主题
subject='python email test'
#构造邮件对象MIMEMultipart对象
msg=MIMEMultipart('mixed')
msg['subject']=subject
msg['Form']='18844141433@163.com'
msg['To']=';'.join(receiver)

#构造文本内容
text="Hi\nthis is python test\n Can you receive email?you can address you problem with\n http://www.baidu.com"
text_plain=MIMEText(text,'plain','utf-8')
msg.attach(text_plain)

#构造图片链接
sendimage=open(r'E:\pythontest\EXO.jpg','rb').read()
image=MIMEImage(sendimage)
image.add_header('Content_ID','<image>')
image["Content-Disposition"]='attachment;filename="EXO.jpg"'
msg.attach(image)

#构造html
html="""
<html>
    <head></head>
    <body>
        <p> Hi<br>
        <a href="http://www.baidu.com></a>
    </body>        
</html>
"""
text_html=MIMEText(html,'html','utf-8')
text_html["Content-disposition"]='attachment;filename=texthtml.html'
msg.attach(text_html)

#构造附件
send_file=open(r'E:\pythontest\Halloween.txt','rb').read()
text_att=MIMEText(send_file,'base64','utf-8')
text_html["Content-disposition"]='attachment;filename=Halloween.txt'
msg.attach(text_att)
#发送邮件
#登录
try:
    # smtp_server='smtp.163.com'
    # smtp = smtplib.SMTP(smtp_server, 25)
    # smtp.login(username,password)
    # smtp.sendmail(sender,receiver,msg.as_string())
    # smtp.quit()
    print("sendemail success")
    # ssl登录
    smtp = smtplib.SMTP_SSL('smtp.163.com')
    #set_debuglevel(1)是用来调试的。参数值为1表示开启调试模式，参数值为0关闭调试模式
    smtp.set_debuglevel(1)
    smtp.ehlo('smtp.163.com')
    smtp.login(username, password)
    smtp.quit()
    print("sendemail success")
except smtplib.SMTPException:
    print("Error :unale to send email")
