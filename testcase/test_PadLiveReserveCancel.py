import json
import requests
from copy import deepcopy
from testcase.pub import PubTest
from PyMsqlTest.FangFa import TestMysql
import pymysql


class PadLiveReserveCancel(PubTest):

    def test_Cancel_case(self):
        code = requests.request("POST", url=PubTest.PadLiveReserveCancel, data=json.dumps(TestMysql.data2))
        self.assertEquals(code.json(), {'status': 1, "msg": "取消预约成功"})
