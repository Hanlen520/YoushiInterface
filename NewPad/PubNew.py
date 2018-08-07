import json
import unittest
import requests


class TestLogin(unittest.TestCase):
    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    # 登录
    base_url = "https://sit5home.uuabc.com/userlogin"

    # 课程信息
    course_info = "https://sit5home.uuabc.com/stuapi/v/course/info"

    # 用户信息
    student_info = "https://sit5home.uuabc.com/stuapi/v/student/info"

    # 任务卡片
    task_lists = "https://sit5home.uuabc.com/stuapi/v/task/lists"

    # 课程列表
    course_lists = "https://sit5home.uuabc.com/stuapi/v/course/lists"

    #
    finishTask = "https://sit5home.uuabc.com/stuapi/v/task/finshtask"

    # 读取气泡

    read_url = "https://sit5home.uuabc.com/stuapi/v/task/readnotice"

    # 个人中心水平测试对照表

    gradelist = "https://sit5home.uuabc.com/stuapi/v/leveltest/gradelist"

    # 播课回放列表

    livevack = "https://sit5home.uuabc.com/stuapi/v/course/livesback"

    #额外奖励U币
    addgold= "http://sit5home.uuabc.com/stuapi/v/task/addgold"

    #看完视频接口
    sawvideo= "http://sit5home.uuabc.com/stuapi/v/student/sawvideo"

    #设备检测
    devicetest = "http://sit5home.uuabc.com/stuapi/v/task/devicetest"




    headers = {
        'content-type': 'application/json; charset = utf-8',
        'Accept': 'application/json',
        'Cache-Control': 'no-cache',

    }

    data = {
        'phoneNum': '13333333335',
        'password': '123456',
        'version': '3.0.0',
        'appVersion': '3.0.2',
        'deviceUUID': '234',
        'deviceType': 'iPad',
        'systemVersion': '10.3.3',
        'system': 'iOS',
        'type': '1',
    }
    results = requests.request("POST", base_url, headers=headers, params=data)
    ld = json.loads(results.text)
    print(ld)