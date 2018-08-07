import json
import requests
from NewPad.PubNew import TestLogin
from copy import deepcopy


class Lists(TestLogin):
    play = {
        'token': 'MPjAED5_OUAUO0O0OAO0O0OB',
        'uuid': 2,
    }

    def test_lists_case(self):
        code = requests.request("POST", TestLogin.task_lists, data=json.dumps(self.play))
        ss = json.loads(code.text)
        if ss['msg'] == "您还未登录":
            re = deepcopy(self.play)
            re['token'] = TestLogin.ld['token']
            code = requests.request("POST", TestLogin.task_lists, data=json.dumps(re))
            self.assertEquals(code.status_code,200)
        else:
            self.assertEquals(code.status_code, 200)

    def test_json_case(self):
        code = requests.request("POST", TestLogin.task_lists, data=json.dumps(self.play))
        self.assertRaises(TypeError)

    def test_lists_token_error_case(self):
        re = deepcopy(self.play)
        re['token'] = None
        code = requests.request("POST", TestLogin.task_lists, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "您还未登录")

    # def test_uuid_None_case(self):
    #     re = deepcopy(self.play)
    #     re['uuid'] = None
    #     code = requests.request("POST", TestLogin.task_lists, data=json.dumps(re))
    #     ss = json.loads(code.text)
    #     self.assertEquals(ss['msg'], "登录信息失效，请重新登录")

    # def test_uuid_None_case(self):
    #     re = deepcopy(self.play)
    #     re['token'] = None
    #     code = requests.request("POST", TestLogin.task_lists, data=json.dumps(re))
    #     ss = json.loads(code.text)
    #     self.assertRaises(100)

