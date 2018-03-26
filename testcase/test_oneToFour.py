import traceback

import requests
from testcase.pub import PubTest
import unittest
import json
from copy import deepcopy


class OneToFour(unittest.TestCase):
    data = {
        'token': PubTest.ld['token'],
        'version': '3.0.0',
        'type': 1,
    }

    headers = {
        'content-type': 'multipart/form-data;',
        'accept': 'application/json',
    }

    def setUp(self):
        print("start")

    def tearDown(self):
        print("end")

    def test_oneToFour_case(self):

        code = requests.request("POST", headers=self.headers, url=PubTest.one_url, params=self.data)
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_OneToFour_token_None_case(self):
        re = deepcopy(self.data)
        re['token'] = None
        code = requests.request("POST", headers=self.headers, url=PubTest.one_url, params= re)
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'],"请先登录")

    # type=2 一对四学习记录
    def test_OneToFour_study_case(self):
        re = deepcopy(self.data)
        re['type'] = 2
        code = requests.request("POST", headers=self.headers, url=PubTest.one_url, params=re)
        ss = json.loads(code.text)
        try:
            if ss['status'] == 1:
                if ss['courseInfo']:
                    pass
                else:
                    raise Exception("没有学习记录")
                pass
            else:
                raise Exception("status ==0")
        except:
            traceback.print_exc()

