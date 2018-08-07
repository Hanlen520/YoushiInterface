import json
import requests
from NewPad.PubNew import TestLogin
from copy import deepcopy


class CourseLists(TestLogin):
    play = {
        'token': TestLogin.ld['token'],
        'classType': None,
        'learning': None,
        'pagesize': None,
        'pageIndex': None,
        'lastTime': None,
        'format': None,
    }

    def test_courseLists_case(self):
        code = requests.request("POST", TestLogin.course_lists, data=json.dumps(self.play))
        self.assertEquals(code.status_code, 200)

    def test_pageSize_case(self):
        code = requests.request("POST", TestLogin.course_lists, data=json.dumps(self.play))
        ss = json.loads(code.text)
        if ss['data']['lists']:
            print(ss['data']['lists'])
        else:
            self.assertEquals(ss['data']['pageInfo']['pageSize'], 100)

    def test_CourseLists_list_case(self):
        code = requests.request("POST", TestLogin.course_lists, data=json.dumps(self.play))
        self.assertIn('data', code.json())

    def test_CourseLists_PageSize_case(self):
        code = requests.request("POST", TestLogin.course_lists, data=json.dumps(self.play))
        self.assertIn('code', code.json())

    def test_CourseLists_lastTime_case(self):
        code = requests.request("POST", TestLogin.course_lists, data=json.dumps(self.play))
        self.assertIn('msg', code.json())

    def test_course_token_error_case(self):
        re = deepcopy(self.play)
        re['token'] = 1231231313131
        code = requests.request("POST", TestLogin.course_lists, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "登录信息失效，请重新登录")

    def test_allLists_case(self):
        re = deepcopy(self.play)
        re['classType'] = None
        re['learning'] = 2
        code = requests.request("POST", TestLogin.course_lists, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "成功")
