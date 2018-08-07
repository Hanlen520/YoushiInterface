import pymysql

# conn = pymysql.connect(host="10.63.0.30",
#                        user="root",
#                        password="root",
#                        db="uu_develop_bak",
#                        port=3306,
#                        charset='utf8'
#                        )

# sit4环境
conn = pymysql.connect(host="sit5home.uuabc.com",
                       user="wufenfen",
                       password="wufenfen",
                       db="uuabc",
                       port=3306,
                       # charset='utf8'
                       )

curse = conn.cursor()
curse.execute("select english_name from student_user where phone = 14700000001")
# curse.execute("SELECT COUNT(*) FROM appoint_course")
re = curse.fetchall()
print(re)
curse.close()
conn.close()
