"""
======================
@author:多测师-黄sir
@time:2020/12/20:10:57
@email:hw18983616870@163.com
======================
"""
'''此模块用来组建测试用例'''
import unittest
from cms_api.Cms_Api import Cms_Api
import requests

class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        Cms_Api.set_session(cls.session)
        Cms_Api.get_session()

    def test_assert_login(self):
        self.value = Cms_Api.cms_login()
        # print(self.value)
        assert self.value['msg']=='登录成功！'
    def test_queryUserList(self):
        self.value =Cms_Api.queryUserList()
        # print(self.value)
        assert self.value['msg']=='查询用户成功！'
if __name__ == '__main__':
    unittest.main(verbosity=2)

