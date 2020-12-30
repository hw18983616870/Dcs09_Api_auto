"""
======================
@author:多测师-黄sir
@time:2020/12/20:9:56
@email:hw18983616870@163.com
======================
"""
'''此模块用来组建所有的接口请求'''
import requests
from config.config import *
# session = requests.Session()
class Cms_Api:

    # 在构造函数中创建一个session，用来保持会话状态
    @classmethod
    def set_session(cls,session) -> None:     #单例模式
        cls.session = session

    @classmethod
    def get_session(cls):
        return cls.session

    # 组建一个登录接口post请求
    @classmethod
    def cms_login(cls):
        cls.response =cls.session.post(url=login_url,
                                         data=login_data,
                                         headers=cms_headers)
        # print(cls.response.text)
        return cls.response.json()   #调用.json方法把响应体的内容转换成字典格式
#     组建一个用户查询接口
    @classmethod
    def queryUserList(cls):
        cls.response = cls.session.post(url=queryUserList_url,
                                          data=queryUserList_data,
                                          headers=cms_headers)
#         print(cls.response.text)
        return cls.response.json()   #调用.json方法把响应体的内容转换成字典格式
if __name__ == '__main__':

    Cms_Api.set_session(session)
    Cms_Api.get_session()
    Cms_Api.cms_login()

    # c.cms_login()
    # c.queryUserList()














