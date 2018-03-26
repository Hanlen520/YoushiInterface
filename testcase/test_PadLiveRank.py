import json
import requests
from testcase.pub import PubTest
from copy import deepcopy


class PadLiveRank(PubTest):
    play = {
        'token': PubTest.ld['token'],
        'course_id': 1,
    }

    def test_Rank_case(self):
        re = deepcopy(self.play)
        code = requests.request("POST", url=PubTest.PadLiveRank, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "操作成功")

    def test_Rank_token_error_case(self):
        re = deepcopy(self.play)
        re['token'] = None
        code = requests.request("POST", url=PubTest.PadLiveRank, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "请先登录")

    def test_Rank_id_error_case(self):
        re = deepcopy(self.play)
        re['course_id'] = None
        code = requests.request("POST", url=PubTest.PadLiveRank, data=json.dumps(re))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "直播课id不能为空")
