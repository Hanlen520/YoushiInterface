import traceback
import requests
import json
from copy import deepcopy
from testcase.pub import PubTest


class PadLivePlaybackCase(PubTest):

    play = {
        'token': PubTest.ld['token'],
        'page': 1,
    }

    def test_back_case(self):
        code = requests.request("POST", url=PubTest.PadLivePlayback, data=json.dumps(self.play))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 1)

    def test_back_token_error_case(self):
        re = deepcopy(self.play)
        re['token'] = 12355
        code = requests.request("POST", url=PubTest.PadLivePlayback, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['status'], 0)

    def test_back_list_case(self):
        code = requests.request("POST", headers=self.headers, url=PubTest.PadLivePlayback, data=json.dumps(self.play))
        ss = json.loads(code.text)
        try:
            if ss['status'] == 1:
                if ss['list']:
                    pass
                else:
                    raise Exception("没有已看记录")
                pass
            else:
                raise Exception("status ==0")
        except:
            traceback.print_exc()
