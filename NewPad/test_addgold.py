import json
import requests
from NewPad.PubNew import TestLogin
from copy import deepcopy


class AddGold(TestLogin):

    data = {
        "token":TestLogin.ld["token"],
        "type":"1",
        "classId":"",
        "classType":""
    }

    def test_addgold(self):
        code = requests.request("POST",TestLogin.addgold,headers=TestLogin.headers,data=self.data)
        self.assertEquals(code.status_code,200)
