# import os
# from HTMLTestRunner import HTMLTestRunner
# from email.mime.text import MIMEText
# from email.header import Header
# import smtplib
# import unittest
# import time
#
# # 定义文件目录
# result_dir = "/Users/shuibu/PycharmProjects/YoushiInterface/test_result/"
#
# lists = os.listdir(result_dir)  # 获取该目录下的所有文件、文件夹，保存为列表
#
# # 对目录下的文件按创建的时间进行排序
# lists.sort(key=lambda fn: os.path.getmtime(result_dir + "\\" + fn))
# # lists[-1]取到的是最新生成的文件或文件夹
# print(('最新的文件是：' + lists[-1]))
# file = os.path.join(result_dir, lists[-1])
#
# print(file)
#
#
#
#
#
# if __name__ == "__main__":
#     test_dir = "测试用例存放目录"
#     test_report = "测试报告存放目录"
#
#     discover = unittest.defaultTestLoader.discover(test_dir,
#                                                    pattern='test_*.py')
#     now = time.strftime("%Y-%m-%d_%H-%M-%S")
#     filename = test_report + '/' + now + 'result.html'
#     fp = open(filename, 'wb')
#     runner = HTMLTestRunner(stream=fp,
#                             title='测试报告',
#                             description='用例执行情况：')
#     runner.run(discover)
#     fp.close()
#
#     new_report = new_report(test_report)
#     send_mail(new_report)  # 发送测试报告