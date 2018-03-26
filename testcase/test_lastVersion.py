# -*- coding: UTF-8 -*-
import requests
from testcase.pub import PubTest
import json
import demjson
from copy import deepcopy


class LastVersion(PubTest):
    play = {
        'appVersion': '3.0.1',
        'system': 'iOS',
        'appType': '1',
        'version': '3.0.0',
    }

    def test_version_case(self):
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(self.play))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_appVersionNone_case(self):
        re = deepcopy(self.play)
        re['appVersion'] = None
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_appVersionError_case(self):
        re = deepcopy(self.play)
        re['appVersion'] = 100000000.000
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_appVersionString_case(self):
        re = deepcopy(self.play)
        re['appVersion'] = "你好"
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_systemNone_case(self):
        re = deepcopy(self.play)
        re['system'] = None
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 0)

    def test_systemError_case(self):
        re = deepcopy(self.play)
        re['system'] = 12345678
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 0)

    def test_systemString_case(self):
        re = deepcopy(self.play)
        re['system'] = "你好"
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 0)

    def test_appTypeNone_case(self):
        re = deepcopy(self.play)
        re['appType'] = None
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_appTypeError_case(self):
        re = deepcopy(self.play)
        re['appType'] = '12345678'
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(demjson.encode
                                                                                                          (re)))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 0)

    def test_appTypeString_case(self):
        re = deepcopy(self.play)
        re['appType'] = '你好'
        code = requests.request("POST", url=PubTest.lastVersion, headers=PubTest.headers, data=json.dumps(demjson.encode
                                                                                                          (re)))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 0)
