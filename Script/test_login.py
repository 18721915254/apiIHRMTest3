import unittest
import logging

from API.login_api import LoginApi
from utils import assert_common


class TestIHRMLogin(unittest.TestCase):
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

    def test02_uesrname_is_not_exist(self):
        response = self.login_api.login("18721915254", "123456")
        jsonDate = response.json()
        logging.info("账号不存在时输入的数据为：{}".format(jsonDate))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test03_password_wrong(self):
        response = self.login_api.login("13800000002", "error")
        jsonDate = response.json()
        logging.info("密码错误时返回数据为：{}".format(jsonDate))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")

    def test04_username_have_special(self):
        response = self.login_api.login("*&*^^&%^%^%^%^%^%^%^%^%^%^%%%%%%%%%%%%%%%%%%%%%%%%%%%", "error")
        jsonDate = response.json()
        logging.info("输入特殊字符时返回数据为：{}".format(jsonDate))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    def test05_zhanghao_is_none(self):
        response = self.login_api.login("", "123456")
        jsonDate = response.json()
        logging.info("账号为空时返回数据为：{}".format(jsonDate))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    def test06_password_is_none(self):
        response = self.login_api.login("13800000002", "")
        jsonDate = response.json()
        logging.info("密码为时返回数据为：{}".format(jsonDate))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    def test07_hanghao_have_cheinese(self):
        response = self.login_api.login("13800中国0002", "123456")
        jsonDate = response.json()
        logging.info("账号有中文时返回数据为：{}".format(jsonDate))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")
    def test08_hanghao_have_kongge(self):
        response = self.login_api.login("13800 0002", "123456")
        jsonDate = response.json()
        logging.info("账号有空格时返回数据为：{}".format(jsonDate))
        assert_common(self, response, 200, False, 20001, "用户名或密码错误")