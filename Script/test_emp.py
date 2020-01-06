import unittest

import logging

import app
from API.emp_api import EmApi
from utils import assert_common, read_add_emp_data
from parameterized import parameterized

class TestIHRMMEmp(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.emp_api = EmApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    @parameterized.expand(read_add_emp_data)
    def test01_add_emp(self,username,mobile,success,code,message,http_code):
        response=self.emp_api.add_emp(username,mobile)
        jsonData=response.json()
        logging.info("添加员工接口返回数据 ： {}".format(jsonData))
        assert_common(self,response,http_code,success,code,message)
        app.EMP_ID=jsonData.get("date").get("id")
        logging.info("员工id：{}".format(jsonData))
    def test02_query_emp(self):
        # 调用查询接口
        response = self.emp_api.query_emp()
        jsonDate = response.json()
        logging.info("登陆成功返回的数据：{}", format(jsonDate))
        assert_common(self, response, 200, True, 10000, "操作成功")

    def test03_modify_emp(self):
        response = self.emp_api.modify_emp("你猜")
        jsonDate = response.json()
        logging.info("修改员工返回的数据：{}", format(jsonDate))
        assert_common(self, response, 200, True, 10000, "操作成功")
    def test04_delete_emp(self):
        response = self.emp_api.query_emp()
        jsonDate = response.json()
        logging.info("删除员工返回的数据：{}", format(jsonDate))
        assert_common(self, response, 200, True, 10000, "操作成功")
