import requests
import json
from testcase.pub import PubTest
from copy import deepcopy


class MyClassInfo(PubTest):
    play = {
        'token': PubTest.ld['token'],
        'version': '3.0.0',

    }

    def test_MyClassInfo_classInfo_case(self):
        code = requests.request("POST", url=PubTest.myClassInfo, headers=PubTest.headers, data=json.dumps(self.play))
        self.assertIn('classInfo', code.json())

    def test_MyClassInfo_page_case(self):
        code = requests.request("POST", url=PubTest.myClassInfo, headers=PubTest.headers, data=json.dumps(self.play))
        print(code.json())
        self.assertIn('page', code.json())

    def test_MyClassInfo_msg_case(self):

        code = requests.request("POST", url=PubTest.myClassInfo, headers=PubTest.headers, data=json.dumps(self.play))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], 'Ok')

    def test_MyClassInfo_tokenError_case(self):
        re = deepcopy(self.play)
        re['token'] = None
        code = requests.request("POST", url=PubTest.myClassInfo, headers=PubTest.headers, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'],2)

