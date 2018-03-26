import os
from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time

test_dir = '/Users/shuibu/PycharmProjects/YoushiInterface/testcase/'


# ==============定义发送邮件==========

def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['Subject'] = Header("iPad接口测试报告(部分)", 'utf-8')

    smtp = smtplib.SMTP()
    smtp.connect('smtp.exmail.qq.com')  # 邮箱服务器
    smtp.login("yao.li@uuabc.com", "Liyao121673")  # 登录邮箱
    #  smtp.sendmail("yao.li@uuabc.com", "testgroup@uuabc.com", msg.as_string())  # 发送者和接收者
    smtp.sendmail("yao.li@uuabc.com", "yao.li@uuabc.com", msg.as_string())  # 发送者和接收者
    smtp.quit()
    print("邮件已发出！注意查收。")


# ======查找测试目录，找到最新生成的测试报告文件======
def new_report(test_report):
    lists = os.listdir(test_report)  # 列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn: os.path.getmtime(test_report + "/" + fn))  # 按时间排序
    file_new = os.path.join(test_report, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)
    return file_new


if __name__ == '__main__':
    test_report = "test_result"

    suite = unittest.defaultTestLoader.discover(test_dir, pattern='test*.py')
    now = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))
    filename = '/Users/shuibu/PycharmProjects/YoushiInterface/test_result/' + now + 'test_result.html'
    fp = open(filename, 'wb+')
    runner = HTMLTestRunner(fp, title=u'测试用例(uathome环境)', description=u'report test')
    runner.run(suite)
    fp.close()

    new_report = new_report(test_report)
    send_mail(new_report)  # 发送测试报告
