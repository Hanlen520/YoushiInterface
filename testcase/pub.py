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

    conn = pymysql.connect(host="sit5home.uuabc.com",
                           user="wufenfen",
                           password="wufenfen",
                           db="uuabc",
                           port=3306,
                           charset='utf8'
                           )
    cursor = conn.cursor()
    cur = conn.cursor()
    cursor.execute("select max(id) from live_course WHERE status=1 ")
    cur.execute("select max(live_id) from live_reserve WHERE disabled =0 ")
    dock = cursor.fetchall()
    dock2 = cur.fetchall()
    for raw in dock:
        for row in dock2:
            if raw != row:
                cursor.execute("select max(id) from live_course WHERE status=1 ")
            else:
                cur.execute("delete from live_reserve where student_id=1952 ORDER BY update_at DESC limit 1")

    cur.close()
    cursor.close()
    conn.close()

    data2 = {
        'liveId': raw[0],
        'token': ld['token'],
    }

    def setUp(self):
        print("testing start")

    def tearDown(self):
        print("testing end")
