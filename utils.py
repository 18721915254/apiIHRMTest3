import pymysql

import app
import json


def assert_common(self, response, http_code, success, code, message):
    # 断言
    self.assertEqual(http_code, response.status_code)
    self.assertEqual(success, response.json().get("success"))
    self.assertEqual(code, response.json().get("code"))
    self.assertIn(message, response.json().get("message"))


def read_login_data():
    data_path = app.BASE_DIR + "/Data/login_data.json"
    with open(data_path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        p_list = []
        for data in jsonData:
            mobile = data.get("mobile")
            password = data.get("password")
            http_code = data.get("http_code")
            success = data.get("success")
            code = data.get("code")
            message = data.get("message")
            p_list.append(
                (mobile, password, http_code, success, code, message)
            )
    print(p_list)
    return p_list


def read_add_emp_data():
    path = app.BASE_DIR + "/Data/empolyee.json"
    with open(path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        add_emp_data = jsonData.get("add_emp")
        result_list = []
        username = add_emp_data.get("username")
        mobile = add_emp_data.get("mobile")
        success = add_emp_data.get("success")
        code = add_emp_data.get("code")
        message = add_emp_data.get("message")
        http_code = add_emp_data.get("http_code")
        result_list.append((username, mobile, success, code, message, http_code))
    print("读取的数据为：", result_list)
    return result_list


def read_query_emp_data():
    path = app.BASE_DIR + "/Data/empolyee.json"
    with open(path, mode="r", encoding="utf-8") as f:
        jsonData = json.load(f)
        result_list = []
        query_emp_data = jsonData.get("uery_emp")
        mobile = query_emp_data.get("mobile")
        success = query_emp_data.get("success")
        code = query_emp_data.get("code")
        message = query_emp_data.get("message")
        http_code = query_emp_data.get("http_code")


class DBuntils:
    def __init__(self, host="182.92.81.159", uesr="readuser", password="iHRM_uesr_2019", database="ihrm"):
        self.host = host
        self.user = uesr
        self.password = password
        self.database = database

    def __enter__(self):
        self.conn = pymysql.connect(self.host, self.user, self.password, self.database)
        self.cursor = self.conn.cursor()
        return self.cursor

    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.cursor:
            self.cursor.close()

        if self.conn:
            self.conn.close()


if __name__ == '__main__':
    read_login_data()
