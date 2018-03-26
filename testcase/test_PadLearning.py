import json
from copy import deepcopy
from testcase.pub import PubTest
import requests
import unittest


class OneToOneCase(PubTest):

    play = {
        'token': PubTest.ld['token'],
        'type': 1,
        'page': 1,
    }

    def test_OneToOne_case(self):
        code = requests.request("POST", headers=PubTest.headers, url=PubTest.one_to_one_url, data=json.dumps(self.play))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    # type =2 学习记录
    def test_OnrToOne_Type2_case(self):
        re = deepcopy(self.play)
        re['type'] = 2
        code = requests.request("POST", headers=PubTest.headers, url=PubTest.one_to_one_url, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertTrue(ss['total'])
