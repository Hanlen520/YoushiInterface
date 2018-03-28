import json
import requests
from copy import deepcopy
from testcase.pub import PubTest
import traceback
from PyMsqlTest.FangFa import TestMysql


class PadLiveReserve(PubTest):

    def test_Reserve_case(self):
        code = requests.request("POST", url=PubTest.PadLiveReserve, data=json.dumps(TestMysql.data2))
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
        re = deepcopy(TestMysql.data2)
        re['liveId'] = 1000
        code = requests.request("POST", url=PubTest.PadLiveReserve, data=json.dumps(re))
        self.assertEquals(code.json(), {"status": 0, "msg": "直播课不存在"})

    def test_reserve_seek_case(self):
        code = requests.request("POST", url=PubTest.PadLiveReserve, data=TestMysql.data2)
        ss = json.loads(code.text)
        self.assertEquals(ss["msg"],"预约成功")



