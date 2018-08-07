import pymysql
import json
import requests
from PyMsqlTest.FangFa import TestMysql
from testcase.pub import PubTest
from copy import deepcopy


class PadLiveHistory(PubTest):
    play = {
        'token': PubTest.ld['token'],
        'page': '',
        'level': '',
    }

    def test_History_case(self):
        code = requests.request("POST", url=PubTest.PadLiveHistory, data=json.dumps(self.play))
        ss = json.loads(code.text)
        self.assertEquals(code.status_code,200)

    def test_History_pageError_case(self):
        re = deepcopy(self.play)
        re['page'] = 'dd'
        code = requests.request("POST", url=PubTest.PadLiveHistory, data=re)
        ss = json.loads(code.text)
        self.assertEquals(ss["msg"],"操作成功")
