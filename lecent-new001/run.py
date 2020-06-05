import unittest,time
from utils.HTMLTestReportCN import HTMLTestRunner
import utils.util as ut
import os
import smtplib
from email.mime.text import MIMEText
from email.header import Header

def run_case(casepath):
    case = unittest.defaultTestLoader.discover(casepath, pattern='test*.py', top_level_dir=None)
    now = time.strftime("%Y-%m-%d %H-%M-%S", time.localtime(time.time()))
    report = open(ut.REPORT_PATH + '/' + now + '.html', 'wb')
    runner = HTMLTestRunner(stream=report, title='新资管理后台自动化测试报告', description='用例执行情况')
    runner.run(case)
    report.close()

def send_mail(title2,sender, psw, receiver, smtpserver,reportfile, port=465):
    '''发送最新的测试报告内容'''
    #打开测试报告
    lists = os.listdir(reportfile)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(reportfile + "/" + fn))  # 按时间排序
    file_new = os.path.join(reportfile, lists[-1])  # 获取最新的文件保存到file_new
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()
    # 定义邮件内容
    msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
    msg['Subject'] = Header(title2, 'utf-8')
    # 这里的to_address只用于显示，必须是一个string
    msg['To'] = receiver
    msg['From'] = sender

    try:
        smtp = smtplib.SMTP_SSL(smtpserver, port)
        smtp.login(sender, psw)
        # 这里的to_address是真正需要发送的到的mail邮箱地址需要的是一个list
        smtp.sendmail(sender, receiver, msg.as_string())
        print('%s----发送邮件成功' % time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
    except Exception as err:
        print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))
        print(err)
    # 用户名密码
    smtp.login(sender, psw)
    smtp.sendmail(sender, receiver, msg.as_string())
    smtp.quit()
if __name__ == '__main__':
    casepath = ut.TESTCASE_PATH
    run_case(casepath)
    title2 = "新资管管理后台主流程业务自动化回归测试报告"
    reportfile = ut.REPORT_PATH #测试报告路径
    smtpserver = "smtp.163.com"  #  邮箱服务器
    sender = "18798799483@163.com" # 自己的账号
    psw = "myy0718" #自己的密码
    receiver = "qq16684810718@163.com" #对方的账号
    send_mail(title2, sender, psw, receiver, smtpserver, reportfile)
