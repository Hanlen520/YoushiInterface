from locust import HttpLocust, TaskSet, task
import json


class UserTasks(TaskSet):

    @task(1)
    def index(self):
        # self.client.post("/stuapi/v/task/lists")
        request_url=("/stuapi/v/task/lists")
        request_params={
            "token":"MPjAED5_OUAUO0O0OAO0O0OB",
            "uuid":"1231"
        }
        request_headers={
            "Accept": "application/json"
        }
        response=self.client.post(
            url=request_url,
            params=json.dumps(request_params),
            headers=request_headers
        )
        r=json.loads(response.text)

        if r["status"] != 1:
            print("接口返回异常" + r["status"] + request_url)
        else:
            pass

    # @task(1)
    # def index1(self):
    #     request_url=("/many/readSpeak")
    #     request_params={
    #         "sendId": "48771",
    #         "sendType": "1",
    #         "classId": "224",
    #         "receiveType": "1",
    #         "new": "1"
    #     }
    #     request_headers={
    #         "Accept": "application/json"
    #     }
    #     response=self.client.post(
    #         url=request_url,
    #         params=request_params,
    #         headers=request_headers
    #     )
    #     r=json.loads(response.text)
    #     if r["status"] != 1:
    #         print("接口返回异常" + r["status"] + request_url)
    #     else:
    #         pass

    # @task(1)
    # def index1(self):
    #     request_url=("/many/classIn")
    #     request_params={
    #         "userId": "48771",
    #         "userType": "1",
    #         "classId": "224",
    #         "platform": "1",
    #         "new": "1"
    #     }
    #     request_headers={
    #         "Accept": "application/json"
    #     }
    #     response=self.client.post(
    #         url=request_url,
    #         params=request_params,
    #         headers=request_headers
    #     )
    #     r=json.loads(response.text)
    #     if r["info"] != "ok":
    #         # response.failure("Failed!")
    #         print("接口返回异常" + r["info"] + request_url)
    #     else:
    #         pass

        # @task(1)
        # def index3(self):
        #     request_url=("/many/classOut")
        #     request_params={
        #         "userId": "681",
        #         "userType": "2",
        #         "classId": "53",
        #         "outPage": "5",
        #         "new": "1"
        #     }
        #     request_headers={
        #         "Accept": "application/json"
        #     }
        #     response=self.client.post(
        #         url=request_url,
        #         params=request_params,
        #         headers=request_headers
        #     )
        #     r=json.loads(response.text)
        #     if r["status"] != 1:
        #         print("接口返回异常" + r["status"] + request_url)
        #     else:
        #         pass


class WebsiteUser(HttpLocust):
    weight=1
    host="https://sit5home.uuabc.com"
    min_wait=2000
    max_wait=5000
    task_set=UserTasks