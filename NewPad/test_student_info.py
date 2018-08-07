import requests
import json
from NewPad.PubNew import TestLogin
from copy import deepcopy


class StudentInfo(TestLogin):
    play = {
        'token': 'MPjAED5_OUAUO0O0OAO0O0OB',
    }

    def test_studentInfo_case(self):
        code = requests.request("POST", url=TestLogin.student_info, headers=TestLogin.headers,
                                data=json.dumps(self.play))
        self.assertEquals(code.status_code, 200)

    def test_studentInfo_userId_case(self):
        code = requests.request("POST", url=TestLogin.student_info, headers=TestLogin.headers,
                                data=json.dumps(self.play))
        self.assertIn('data', code.json())

    def test_studentInfo_token_None_case(self):
        re = deepcopy(self.play)
        re['token'] = None
        code = requests.request("POST", url=TestLogin.student_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "您还未登录")

    def test_info_error(self):
        re = deepcopy(self.play)
        re['token'] = 12313132132132
        code = requests.request("POST", url=TestLogin.student_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "登录信息失效，请重新登录")
