from pip.utils import logging

import app
from utils import assert_common

import unittest
import logging

from API.login_api import LoginApi
from utils import assert_common


class Login(unittest.TestCase):
    def setUp(self) -> None:
        pass

    @classmethod
    def setUpClass(cls) -> None:
        cls.login_api = LoginApi()

    def tearDown(self) -> None:
        pass

    @classmethod
    def tearDownClass(cls) -> None:
        pass

    def test01_login_success(self):
        response = self.login_api.login("13800000002", "123456")
        jsonData = response.json()

        logging.info("登录成功返回数据 ： {}".format(jsonData))

        # 断言
        # self.assertEqual(200, response.status_code)
        # self.assertEqual(True, jsonData.get("success"))
        # self.assertEqual(10000, jsonData.get("code"))
        # self.assertIn("操作成功", jsonData.get("message"))
        assert_common(self, response, 200, True, 10000, "操作成功")
def test_login(self):
    response=self.login.api.login("13800000002","123456")
    jsonDate=response.json()
    logging.info("登陆成功返回的数据：{}",format(jsonDate))
    assert_common(self,response,200,True,10000,"操作成功")
    token=jsonDate.get("date")
    app.HEADERS["Autherization"]="Bearer" + token
    logging.info("保存的令牌时：{}".format(app.HEADERS))