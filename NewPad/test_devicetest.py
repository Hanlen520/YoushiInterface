import requests
import unittest
from NewPad.PubNew import TestLogin


class DeviceTest(TestLogin):

    data = {
        "token":TestLogin.ld["token"],
        "uuid":1231,
        "end":1,
        "endName":1,
        "endVersion":10.3,
        "appVersion":None
    }

    def test_device(self):

        code = requests.post(TestLogin.devicetest,data=self.data)
        self.assertEquals(code.status_code,200)
