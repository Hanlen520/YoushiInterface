# import smtplib
# from email.mime.text import MIMEText  # MIMEText()定义邮件正文
# from email.header import Header  # Header()定义邮件标题
#
# # 发送邮箱服务器
# smtpserver = 'smtp.exmail.qq.com'
#
# # 发送邮箱用户/密码(登录邮箱操作)
# user = "yao.li@uuabc.com"
# password = "password"
#
# # 发送邮箱
# sender = "yao.li@uuabc.com"
#
# # 接收邮箱
# receiver = "muzi379178228@qq.com"
#
# # 发送主题
# subject = 'email by  python'
#
# # 编写HTML类型的邮件正文（把HTML代码写进入）
# msg = MIMEText('<html><body><a href="">百度一下</a></p></body></html>', 'html', 'utf-8')
# msg['Subject'] = Header(subject, 'utf-8')
#
# # 连接发送邮件<strong><span style="color:#ff6666;">（smtplib模块基本使用格式）</span></strong>
# smtp = smtplib.SMTP()
# smtp.connect(smtpserver)
# smtp.login(user, password)
# smtp.sendmail(sender, receiver, msg.as_string())
# smtp.quit()
