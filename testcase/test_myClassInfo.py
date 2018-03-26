import requests
import json
from testcase.pub import PubTest
from copy import deepcopy


class MyClassInfo(PubTest):
    play = {
        'token': PubTest.ld['token'],
        'version': '3.0.0',

    }

    def test_MyClassInfo(self):
        code = requests.request("POST", url=PubTest.myClassInfo, headers=PubTest.headers, data=json.dumps(self.play))
        self.assertIn('classInfo', code.json())

