‘’‘
发送邮件通知
’‘’

import smtplib
from email.mime.text import MIMEText

class Email_notifier:
    '''描述一个邮件发送工具
    
    可以利用add和pw变量来自定义邮箱地址和邮箱密码，利用content变量来自定义邮件内容。
    '''

    def __init__(self):
        '''title题目
        content内容
        sender发送邮箱
        receivers接受邮箱
        pw发送邮箱密码
        mail_host发送邮箱发送服务器地址
        '''
        self.title = 'email_notifier'
        self.content = 'The work is finished'
        self.sender = 'nothing@nothing.com'
        self.receivers = 'nothing@nothing.com'
        self.pw = '123'
        self.mail_host = 'smtp.office365.com'

    def sendEmail(self):
        mail_host = self.mail_host
        # 邮箱信息
        mail_pass = self.pw
        sender = self.sender
        receivers = self.receivers

        # 设置email信息
        message = MIMEText(self.content, 'plain', 'utf-8')
        message['Subject'] = self.title
        message['From'] = sender
        message['To'] = receivers[0]

        # 登录并发送邮件
        try:
            smtpObj = smtplib.SMTP(host=mail_host)
            smtpObj.connect(mail_host, 587)
            smtpObj.set_debuglevel(True)
            smtpObj.starttls()
            smtpObj.login(sender, mail_pass)
            smtpObj.sendmail(
                sender, receivers, message.as_string()
            )
            # 退出
            smtpObj.quit()
            print('success')
        except smtplib.SMTPException as e:
            print('error:', e)  # 打印错误
        return
