import smtplib
from email.mime.text import MIMEText
from email.header import Header


def send(title, link):
    mail_host = "smtp.zju.edu.cn"  # 设置服务器
    mail_user = "21521029"  # 用户名
    mail_pass = "20899100627"  # 口令

    sender = 'hudi@zju.edu.cn'
    receivers = ['hudi@zju.edu.cn']
    message = MIMEText('22223关于英语机考的网页有更新哦～\n最新信息：' + title + '\n(' + link + ') \n'+
                       '要点这里确认所有信息哦\n(http://grs.zju.edu.cn/search.php?postflag=1&area=10001&kw_qbzc=%E6%9C%BA%E8%80%83)', \
                       'plain', 'utf-8')
    message['From'] = Header("小胡迪AI", 'utf-8')
    message['To'] = Header("胡迪", 'utf-8')

    subject = '关于英语机考的通知哦'
    message['Subject'] = Header(subject, 'utf-8')

    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect(mail_host, 25)  # 25 为 SMTP 端口号
        smtpObj.login(mail_user, mail_pass)
        smtpObj.sendmail(sender, receivers, message.as_string())
        print("邮件发送成功")
    except smtplib.SMTPException:
        print("Error: 无法发送邮件")


