import requests
import json
from testcase.pub import PubTest
from copy import deepcopy
from PyMsqlTest.FangFa import TestMysql


class CourseRankList(PubTest):

    play = {
        'courseId': TestMysql.re_dock[0],
        'version': '3.0.0',
        'token': PubTest.ld['token'],
    }

    def test_list_case(self):
        code = requests.request("POST", url=PubTest.CourseRankList,headers=PubTest.headers,data=json.dumps(self.play))
        ss = json.loads(code.text)
        print(ss)
        self.assertEquals(ss['msg'], "Ok")

    # def test_list_courseIdNone_case(self):
    #     re = deepcopy(self.play)
    #     re['courseId'] = None
    #     code = requests.request("POST", url=PubTest.CourseRankList, headers=PubTest.headers, data=json.dumps(re))
    #     ss = json.loads(code.text)
    #     self.assertEquals(ss['msg'], "课程ID不能为空")

    # def test_list_tokenNone_case(self):
    #     re = deepcopy(self.play)
    #     re['token'] = None
    #     code = requests.request("POST", url=PubTest.CourseRankList, headers=PubTest.headers, data=json.dumps(re))
    #     ss = json.loads(code.text)
    #     self.assertEquals(ss['msg'],"请先登录")
