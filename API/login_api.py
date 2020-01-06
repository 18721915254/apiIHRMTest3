# import  requests
# # import  app
# #
# # class LoginApi:
# #     def __init__(self):
# #         self.login_url = app.HOST + "/api/sys/login"
# #         self.headers=app.HEADERS
# #        #从外部接受mobile和password
# #
# #
# #     def login(self, mobile, password):
# #         #使用data来接受外部传入的mobile和lassword 拼接成要发送的数据
# #         data={"mobile":mobile,"password":password}
# #
# #         response=requests.post(self.login_url,json=data,headers=self.headers)
# #
# #         return  response
# #
import requests
import app

class LoginApi:
    def __init__(self):
        self.login_url = app.HOST + "/api/sys/login"
        self.headers = app.HEADERS

    # 从外部接收mobile和passowrd
    # 为什么这么写呢？这是因为，如果写成一个参数data来接收
    # 字典数据的话
    # 那么后续进行参数化时，会很不方便，所以改成接收两个变量
    def login(self, mobile, password):
        # 使用data来接收外部传入的mobile和password,拼接成
        # 要发送的数据
        data = {
            "mobile":mobile,
            "password":password
        }
        # 发送登陆请求，
        response = requests.post(self.login_url,
                                 json=data,
                                 headers=self.headers)
        # 返回响应数据
        return response
