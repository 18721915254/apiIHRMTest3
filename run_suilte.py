import time

# from API.emp_api import EmApi
from Script import login
from Tools.HTMLTestRunner import HTMLTestRunner
import  app
from Script.test_login import TestIHRMLogin
from Script.login import Login
from Script.test_emp import TestIHRMMEmp
from Tools.HTMLTestRunner import HTMLTestRunner
import unittest
suite = unittest.TestSuite()
suite.addTest(unittest.makeSuite(login))
suite.addTest(unittest.makeSuite(TestIHRMMEmp))

report_path = app.BASE_DIR+"/report/ihrm{}.html".format(time.strftime("%Y%m%d %H%M%S"))

with open (report_path,mode="wb")as f:
    runner = HTMLTestRunner(f,verbosity=1,title="人力资源",description="v1.0.0")


    runner.run(suite)