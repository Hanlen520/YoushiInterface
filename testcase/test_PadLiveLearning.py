import requests
import json
from testcase.pub import PubTest
from copy import deepcopy

'''
学习中心直播课列表
'''


class PadLiveLearningCase(PubTest):
    play = {
        'token': PubTest.ld['token'],
        'page': 1,
        'type': 1,
    }

    #status_code =200
    def test_PadLiveLearning_case(self):
        code = requests.request("POST", url=PubTest.PadLiveLearning_url, data=json.dumps(self.play))
        self.assertEquals(code.status_code, 200)

    # 数据正常情况
    def test_Live_more(self):

        code = requests.request("POST", url=PubTest.PadLiveLearning_url, data=json.dumps(self.play))
        ss = json.loads(code.text)

        try:
            if ss['total'] >= 0 & ss['status'] != 0:
                print("数据666")

            else:
                print("数据异常")

        except Exception as e:
            self.assertEquals(ss['msg'],"操作成功")

    # token丢失
    def test_Live_token_error_case(self):

        re = deepcopy(self.data)
        re['token'] = None
        code = requests.request("POST", url=PubTest.PadLiveLearning_url, data=json.dumps(re))
        ss = json.loads(code.text)
        try:
            if ss['total'] >= 0 & ss['status'] != 0:
                print("数据666")

            else:
                print("数据异常")

        except Exception as e:
            self.assertEquals(ss['msg'], "请先登录") # token失效后，提醒登录

    # 学习记录列表 type=2
    def test_Live_type_error_case(self):
        r = deepcopy(self.play)
        r['type'] = 2
        code = requests.request("POST", url=PubTest.PadLiveLearning_url, data=json.dumps(r))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "操作成功")

    # type = None
    def test_Live_type_None_case(self):
        r = deepcopy(self.play)
        r['type'] = None
        code = requests.request("POST", url=PubTest.PadLiveLearning_url, data=json.dumps(r))
        ss = json.loads(code.text)
        self.assertEquals(ss['msg'], "操作成功")
