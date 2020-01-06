import app
from pip.utils import logging

import app
from utils import assert_common
import requests


class EmApi:
    def __init__(self):
        self.emp_url = app.HOST + "/api/sys/user"
        self.headers = app.HEADERS

    def add_emp(self, uesrname, mobile):
        data = {
            "username": uesrname,
            "mobile": mobile,
            "timeOfEntry": "2019-12-02",
            "formOfEmployment": 1,
            "workNumber": "1234",
            "departmentName": "测试",
            "departmentId": "1210411411066695680",
            "correctionTime": "2019-12-15T16:00:00.000Z"
        }

        #发送员工接口请求
        response = requests.post(self.emp_url, json=data, headers=self.headers)
        return response

    def query_emp(self):
        url=self.emp_url + "/"+app.EMP_ID
        return  requests.get(url,headers=self.headers)

         #修改员工
    def modify_emp(self,username):
        url=self.emp_url+"/"+app.EMP_ID
        data={"uesrname":username}
        return requests.put(url,json=data,headers=self.headers)
         #删除员工
    def delete_emp(self):
        url = self.emp_url + "/" + app.EMP_ID
        return requests.put(url,  headers=self.headers)
