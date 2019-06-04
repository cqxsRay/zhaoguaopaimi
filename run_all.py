"""
执行这个脚本可以实现执行用例，生成报告，发送邮件
"""
import unittest
from common import HTMLTestReportCN
import os
import smtplib
import time
import shutil
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import readConfig
content=readConfig.ReadConfig()
# 获取路径
cur_path = os.path.dirname(os.path.realpath(__file__))
# 测试用例路径
case_path = os.path.join(cur_path, 'testcase')
# 测试报告路径
report_path = os.path.join(cur_path, 'report/')
# 获取最新的测试报告
def get_report():
    # 列举目录下的所有文件
    dirs = os.listdir(report_path)
    dirs.sort()
    # 获取最新的测试报告
    newreportname = dirs[-1]
    # 返回的是测试报告的名字
    return newreportname
# 发送邮件
def send_mail():
    newreport = get_report()
    msg = MIMEMultipart()
    # 邮件的标题
    msg['Subject'] = content.get_email("subject")
    msg['date'] = time.strftime('%a, %d %b %Y %H:%M:%S %z')
    with open(os.path.join(report_path, newreport), 'rb') as f:
        # 读取测试报告的内容
        mailbody = f.read()
    # 将测试报告的内容放在邮件的正文当中
    html = MIMEText(mailbody, _subtype='html', _charset='utf-8')
    # 将测试报告放在附件中发送
    msg.attach(html)
    att1 = MIMEText(mailbody, 'base64', 'gb2312')
    att1["Content-Type"] = 'application/octet-stream'
    # 这里的filename可以任意写，写什么名字，附件的名字就是什么
    att1["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(att1)
    # take_messages()
    # 发送邮件的人
    msg['from'] = content.get_email("sender")
    # 接收邮件的人
    value = content.get_email("receiver")
    receiver = []
    for n in str(value).split("/"):
        receiver.append(n)
    """接收邮件的人：list or tuple"""
    sendTo = receiver
    # 收件人不匿名
    # self.msg['to'] = 'lixiaochao@baofeng.com,liyuanyuan@baofeng.com'  # 收件人和发送人必须这里定义一下，执行才不会报错。
    smtp = smtplib.SMTP()
    # 连接服务器
    smtp.connect(content.get_email("host"))
    # 登录的用户名和密码（注意密码是设置客户端授权码，因为使用用户密码不稳听，有时无法认证成功，导致登录不上，故无法发送邮件。）
    smtp.login(content.get_email("user"), content.get_email("pass"))
    # smtp.sendmail(self.msg['from'], self.msg['to'], self.msg.as_string())
    # 发送邮件
    smtp.sendmail(msg['from'], sendTo, msg.as_string())
    smtp.close()
    print('sendmail success')
if __name__ == "__main__":
    # 构造测试集
    suite = unittest.defaultTestLoader.discover(case_path,'test*.py')
    # 获取当前时间
    now = time.strftime('%Y-%m-%d %H_%M_%S')
    newreport = report_path + now + 'report.html'
    report = report_path + 'HTMLReport.html'
    # 定义测试报告
    runner = HTMLTestReportCN.HTMLTestRunner(title='自动化测试报告',description='用例执行情况：',
                                             stream=open(newreport, 'wb'),verbosity=2)
    # 运行测试用例
    runner.run(suite)
    # 这个的测试报告文件是给jekins用的
    shutil.copyfile(newreport,report)
    # get_report()
    # send_mail()