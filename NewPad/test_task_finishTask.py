import json
import requests
from NewPad.PubNew import TestLogin
from copy import deepcopy
import random


class FinishTask(TestLogin):
    play = {
        'token': TestLogin.ld['token'],
        'classId': '',
        'answers': '',
    }

    def test_finishTask_case(self):
        re = deepcopy(self.play)
        re['token'] = TestLogin.ld['token']
        code = requests.request("POST", TestLogin.finishTask, data=json.dumps(self.play))
        self.assertEquals(code.status_code, 200)

    def test_finishTaskJson_case(self):
        re = deepcopy(self.play)
        code = requests.request("POST",headers=TestLogin.headers,url=TestLogin.finishTask, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertRaises(Exception, self.test_finishTask_case())

    def test_finishTask_json_case(self):
        re = deepcopy(self.play)
        re['token'] = TestLogin.ld['token']
        code = requests.request("POST", TestLogin.finishTask, data=json.dumps(self.play))
        ss = json.loads(code.text)
        self.assertRaises(TypeError, TestLogin.ld['token'], ss['msg'])



