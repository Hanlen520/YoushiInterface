import json
import requests
from copy import deepcopy
from testcase.pub import PubTest
import traceback
import pymysql


class PadLiveReserve(PubTest):
    # conn = pymysql.connect(host="sit5home.uuabc.com",
    #                        user="wufenfen",
    #                        password="wufenfen",
    #                        db="uuabc",
    #                        port=3306,
    #                        charset='utf8'
    #                        )
    # cursor = conn.cursor()
    # cur = conn.cursor()
    # cursor.execute("select max(id) from live_course WHERE status=1 ")
    # cur.execute("select max(live_id) from live_reserve WHERE disabled =0 ")
    # dock = cursor.fetchall()
    # dock2 = cur.fetchall()
    # #
    # # for raw in dock:
    # #     for row in dock2:
    # #         if raw != row:
    # #             pass
    # #         else:
    # #             cur.execute("delete from live_reserve where student_id=1952 ORDER BY update_at DESC limit 1")
    #
    # for raw in dock:
    #     for row in dock2:
    #         if raw != row:
    #             cursor.execute("select max(id) from live_course WHERE status=1 ")
    #         else:
    #             cur.execute("delete from live_reserve where student_id=1952 ORDER BY update_at DESC limit 1")
    #
    # cur.close()
    # cursor.close()
    # conn.close()
    #
    # play = {
    #     'liveId': raw[0],
    #     'token': PubTest.ld['token'],
    # }

    def test_Reserve_case(self):
        code = requests.request("POST", url=PubTest.PadLiveReserve, data=json.dumps(PubTest.data2))
        ss = json.loads(code.text)
        try:
            if code.status_code == 200:
                if ss['status'] == 1:
                    pass
                else:
                    raise Exception(ss['msg'])
            else:
                raise Exception("status_code != 200")
        except:
            traceback.print_exc()

    def test_reserve_liveIdError_case(self):
        re = deepcopy(PubTest.data2)
        re['liveId'] = 1000
        code = requests.request("POST", url=PubTest.PadLiveReserve, data=json.dumps(re))
        self.assertEquals(code.json(), {"status": 0, "msg": "直播课不存在"})

    def test_reserve_seek_case(self):
        code = requests.request("POST", url=PubTest.PadLiveReserve, data=PubTest.data2)
        ss = json.loads(code.text)
        self.assertEquals(ss["msg"],"预约成功")



