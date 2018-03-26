import unittest, requests
import json
import pymysql


class PubTest(unittest.TestCase):
    # 登录
    base_url = "https://uathome.uuabc.com/userlogin"

    # 一对四学习中心
    one_url = "https://uathome.uuabc.com/oneToFour"

    # 全部界面
    learning_url = "https://uathome.uuabc.com/PadLearningAll"

    # 直播课列表
    live_list_url = "https://uathome.uuabc.com/PadLiveList"

    # 一对一学习中心
    one_to_one_url = "https://uathome.uuabc.com/PadLearning"

    # 退出
    Logout_url = "https://uathome.uuabc.com/PadLogout"

    # 已上直播课列表
    PadLiveLearning_url = "https://uathome.uuabc.com/PadLiveLearning"

    # 已看直播课列表
    PadLivePlayback = "https://uathome.uuabc.com/PadLivePlayback"

    # 直播回放
    PadLiveHistory = "https://uathome.uuabc.com/PadLiveHistory"

    # 我的班级
    myClassInfo = "https://uathome.uuabc.com/myClassInfo"

    # 直播课-答题排行榜
    PadLiveRank = "https://uathome.uuabc.com/PadLiveRank"

    # 预约直播课
    PadLiveReserve = "https://uathome.uuabc.com/PadLiveReserve"

    # 直播课取消预约
    PadLiveReserveCancel = "https://uathome.uuabc.com/PadLiveReserveCancel"

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

    def setUp(self):
        print("testing start")

    def tearDown(self):
        print("testing end")
