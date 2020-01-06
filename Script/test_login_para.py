import unittest
import logging
from API.login_api import LoginApi
from utils import assert_common, read_login_data
from parameterized.parameterized import parameterized


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

    @parameterized.expand(read_login_data)
    def test_login(self, mobile, password, http_code, success, code, message):
        response = self.login_api.login(mobile, password)
        jsonData = response.json()

        logging.info("登录接口返回数据 ： {}".format(jsonData))

        assert_common(self, response, http_code, success, code, message)
