import unittest
import requests
import json
from NewPad.PubNew import TestLogin
from copy import deepcopy


class ReadNotice(TestLogin):
    play={
        "token": TestLogin.ld['token'],
        "tag": 'levelNotice'
    }

    def test_readnotice_case(self):
        code=requests.request("POST", url=TestLogin.read_url, params=self.play)

        self.assertEqual(code.status_code, 200)

    def test_readnotice_msg_case(self):
        code=requests.request("POST", url=TestLogin.read_url, params=self.play)
        ss=json.loads(code.text)
        self.assertEqual(ss["msg"], "成功")

    def test_error_tag_case(self):
        re=deepcopy(self.play)
        re['tag']='llll'
        code=requests.request("POST", url=TestLogin.read_url, params=re)
        ss=json.loads(code.text)
        self.assertEqual(ss["msg"], "数据库操作失败")

    def test_miss_tag_case(self):
        re=deepcopy(self.play)
        re['tag']=None
        code=requests.request("POST", url=TestLogin.read_url, params=re)
        ss=json.loads(code.text)
        self.assertEqual(ss['msg'], "参数缺失")
