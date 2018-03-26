import json
import unittest, requests
from testcase.pub import PubTest
from copy import deepcopy, copy


class LoginCase(PubTest):

    def test_login_case(self):
        re = json.loads(PubTest.results.text)
        print(PubTest.results.status_code)
        self.assertEquals(PubTest.results.status_code, 200)

    def test_loginOk_case(self):
        re = json.loads(PubTest.results.text)
        self.assertEquals(re['msg'], '登录成功')

    def test_login_password_error_case(self):
        data = deepcopy(PubTest.data)
        data['password'] = 1234567
        code = requests.request("POST", PubTest.base_url, headers=PubTest.headers, params=data)
        re = json.loads(code.text)
        self.assertEquals(re['msg'], '密码错误')

    def test_loginStatus_case(self):
        re = json.loads(PubTest.results.text)
        self.assertEquals(re['status'], 1)

    def test_login_number_error_case(self):
        data = deepcopy(PubTest.data)
        data['phoneNum'] = 147000000180
        code = requests.request("POST", PubTest.base_url, headers=PubTest.headers, params=data)
        re = json.loads(code.text)
        self.assertEquals(re['msg'], '请输入有效手机号')

    def test_login_number_miss_case(self):
        data = deepcopy(PubTest.data)
        data['phoneNum'] = None
        code = requests.request("POST", PubTest.base_url, headers=PubTest.headers, params=data)
        re = json.loads(code.text)
        self.assertEquals(re['msg'], '用户名和密码不能为空')

    def test_login_password_miss_case(self):
        data = deepcopy(PubTest.data)
        data['password'] = None
        code = requests.request("POST", PubTest.base_url, headers=PubTest.headers, params=data)
        re = json.loads(code.text)
        self.assertEquals(re['msg'], "用户名和密码不能为空")

    def test_login_version_error_case(self):
        data = deepcopy(PubTest.data)
        data['version'] = None
        code = requests.request("POST", PubTest.base_url, headers=PubTest.headers, params=data)
        re = json.loads(code.text)
        self.assertNotEquals(re['status'], 1)

    def test_login_appVersion_case(self):
        data = deepcopy(PubTest.data)
        data['appVersion'] = None
        code = requests.request("POST", PubTest.base_url, headers=PubTest.headers, params=data)
        re = json.loads(code.text)
        self.assertNotEquals(re['status'], 1)
