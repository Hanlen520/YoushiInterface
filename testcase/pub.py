import unittest, requests
import json
import pymysql


class PubTest(unittest.TestCase):
    # 登录
    base_url = "https://sit5home.uuabc.com/userlogin"

    # 一对四学习中心
    one_url = "https://sit5home.uuabc.com/oneToFour"

    # 全部界面
    learning_url = "https://sit5home.uuabc.com/PadLearningAll"

    # 直播课列表
    live_list_url = "https://sit5home.uuabc.com/PadLiveList"

    # 一对一学习中心
    one_to_one_url = "https://sit5home.uuabc.com/PadLearning"

    # 退出
    Logout_url = "https://sit5home.uuabc.com/PadLogout"

    # 已上直播课列表
    PadLiveLearning_url = "https://sit5home.uuabc.com/PadLiveLearning"

    # 已看直播课列表
    PadLivePlayback = "https://sit5home.uuabc.com/PadLivePlayback"

    # 直播回放
    PadLiveHistory = "https://sit5home.uuabc.com/PadLiveHistory"

    # 我的班级
    myClassInfo = "https://sit5home.uuabc.com/myClassInfo"

    # 直播课-答题排行榜
    PadLiveRank = "https://sit5home.uuabc.com/PadLiveRank"

    # 预约直播课
    PadLiveReserve = "https://sit5home.uuabc.com/PadLiveReserve"

    # 直播课取消预约
    PadLiveReserveCancel = "https://sit5home.uuabc.com/PadLiveReserveCancel"

    # 检测版本更新
    lastVersion = "https://sit5home.uuabc.com/lastversion"

    # 钻石排行榜
    CourseRankList = "https://sit5home.uuabc.com/courseRankList"

    headers = {
        'content-type': 'application/json; charset = utf-8',
        'Accept': 'application/json',
        'Cache-Control': 'no-cache',

    }

    data = {
        'phoneNum': '14700000001',
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

    def setUp(self):
        print("testing start")

    def tearDown(self):
        print("testing end")



