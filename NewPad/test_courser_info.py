import requests
import json
from NewPad.PubNew import TestLogin
from copy import deepcopy
from testcase.pub import PubTest
import unittest


class CourserInfo(TestLogin):
    play = {
        'classType': 3,
        'classId': '192',
        'token': TestLogin.ld['token']
    }

    def test_courserInfo_case(self):
        code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
                                data=json.dumps(self.play))
        self.assertEquals(code.status_code, 200)

    def test_course_Info_error_case(self):
        re = deepcopy(self.play)
        re['token'] = None
        code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "您还未登录")

    def test_classType_error_case(self):
        re = deepcopy(self.play)
        re['classType'] = None
        code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "必填参数为空")

    def test_classType_1_case(self):
        re = deepcopy(self.play)
        re['classType'] = 1
        re['classId'] = 35715
        code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "成功")

    def test_classType_2_case(self):
        re = deepcopy(self.play)
        re['classType'] = 2
        re['classId'] = 35715
        code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        print(code.json())
        self.assertEquals(ss['msg'], "课程信息不存在")

    def test_classType_3_case(self):
        re = deepcopy(self.play)
        re['classType'] = 3
        re['classId'] = 35715
        code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "课程信息不存在")

    def test_classId_error_case(self):
        re = deepcopy(self.play)
        re['classId'] = None
        code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
                                data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "必填参数为空")

    # def test_videoBack_case(self):
    #     re = deepcopy(self.play)
    #     re['classId'] = '98'
    #     re['token'] = 'MPjAIDw_MUAUO0O0OAO0O0OB'
    #     code = requests.request("POST", TestLogin.course_info, headers=TestLogin.headers,
    #                             data=json.dumps(re))
    #     ss = json.loads(code.text)
    #     self.assertEquals( ss['data']['videoBack'], 'https://livevideo.uuabc.com/20170909_Mike.mp4')
