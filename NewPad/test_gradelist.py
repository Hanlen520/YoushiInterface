import unittest
from NewPad.PubNew import TestLogin
import json
import requests
from copy import deepcopy


class GradeList(TestLogin):
    data = {
        "token": TestLogin.ld["token"]
    }

    def test_gradelist(self):
        code=requests.request("POST", TestLogin.gradelist, data=self.data, headers=TestLogin.headers)
        self.assertEquals(code.status_code, 200)

    def test_token_None(self):
        re=deepcopy(self.data)
        re["token"]=None
        code=requests.request("POST", TestLogin.gradelist, data=re, headers=TestLogin.headers)
        ss=json.loads(code.text)
        self.assertEquals(ss["msg"], "您还未登录")

    def test_token_error(self):
        re=deepcopy(self.data)
        re["token"]=123132131
        code=requests.request("POST", TestLogin.gradelist, data=re, headers=TestLogin.headers)
        ss=json.loads(code.text)
        self.assertEquals(ss["msg"], "您还未登录")

    def test_token_data(self):
        code=requests.request("POST", TestLogin.gradelist, data=self.data, headers=TestLogin.headers)
        ss=json.loads(code.text)
        self.assertIsNotNone(self.data)
