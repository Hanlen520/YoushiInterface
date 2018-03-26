import json
import requests
from copy import deepcopy
from testcase.pub import PubTest
import pymysql


class PadLiveReserveCancel(PubTest):
    play = {
        'token': PubTest.ld['token'],
        'liveId': 195,
    }

    def test_Cancel_case(self):
        code = requests.request("POST", url=PubTest.PadLiveReserveCancel, data=json.dumps(self.play))
        self.assertEquals(code.json(), {'status': 0, "msg": "没有直播课程", "result": []})
