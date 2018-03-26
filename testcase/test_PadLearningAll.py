# -*- coding: UTF-8 -*-

from testcase.pub import PubTest
import requests
from copy import deepcopy
import json
import unittest


class PadLearningAll(PubTest):
    re = PubTest.ld['token']
    data = {
        'token': re,
        'version': '3.0.0',
    }
    headers = {
        'content-type': 'application/json; charset = utf-8',
        'Accept': 'application/json',
        'Cache-Control': 'no-cache',
    }

    def test_LearningAll_case(self):
        code = requests.request("POST", url=PubTest.learning_url, headers=self.headers, data=json.dumps(self.data))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_token_error_case(self):
        re = deepcopy(self.data)
        re['token'] = None
        code = requests.request("POST", url=PubTest.learning_url, headers=self.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss["msg"], "请先登录")
