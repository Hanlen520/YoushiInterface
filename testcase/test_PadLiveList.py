import requests
from testcase.pub import PubTest
import json
from copy import deepcopy


class PadLiveListCase(PubTest):
    play = {
        'page': 1,
        'token': PubTest.ld['token'],
        'version': '3.0.0'
    }

    def test_PadLiveList_case(self):
        code = requests.request("POST", headers=PubTest.headers, url=PubTest.live_list_url, data=json.dumps(self.play))
        re = json.loads(code.text)
        self.assertEquals(re['status'], 1)

    def test_PadLiveList_version_error_case(self):
        re = deepcopy(self.play)
        re['version'] = None
        code = requests.request("POST", headers=PubTest.headers,url=PubTest.live_list_url, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "操作成功")

    def test_PadLiveList_token_error_case(self):
        re = deepcopy(self.play)
        re['token'] = None
        code = requests.request("POST",headers=PubTest.headers, url=PubTest.live_list_url, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "请先登录")

