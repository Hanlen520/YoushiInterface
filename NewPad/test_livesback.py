import requests
import json
import unittest
from NewPad.PubNew import TestLogin


class LiveBack(TestLogin):

    data = {
        "token":TestLogin.ld["token"],
        "pageIndex":"",
        "pageSize":"",
        "lastTime":"",
        "status":"1",
        "state":"1",
        "videoBack":""
    }

    def test_Back_case(self):
        code = requests.request("POST",TestLogin.livevack,data=self.data)
        self.assertEquals(code.status_code,200)