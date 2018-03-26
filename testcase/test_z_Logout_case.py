import requests
import json
from testcase.pub import PubTest
from copy import deepcopy


class TestLogoutCase(PubTest):
    play = {
        'token': PubTest.ld['token'],
        'version': '3.0.0',
    }

    def test_Logout_case(self):
        code = requests.request("POST", url=PubTest.Logout_url, headers=PubTest.headers, data=json.dumps(self.play))
        ss = json.loads(code.text)
        print(ss)
        self.assertEquals(ss['msg'], "退出成功")

    def test_Logout_token_error_case(self):
        re = deepcopy(self.play)
        re['token'] = "MPjAED5_OUAUO0O0OAO0O0"
        code = requests.request("POST", url=PubTest.Logout_url, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "请先登录")

    def test_Logout_None_case(self):
        re = deepcopy(self.play)
        re['token'] = None
        code = requests.request("POST", url=PubTest.Logout_url, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "请先登录")
