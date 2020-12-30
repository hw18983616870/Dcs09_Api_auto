"""
======================
@author:多测师-黄sir
@time:2020/12/20:10:57
@email:hw18983616870@163.com
======================
"""
import unittest
from config.config import *
from cms_api.Cms_Api1 import Test_Api
import requests

class Test_Login(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.session = requests.Session()
        Test_Api.set_session(cls.session)
        Test_Api.get_session()

    def test_assert_login(self):
        headers = ('post', login_url, login_data, cms_headers)
        self.value = Test_Api.test_api(headers)
        # print(self.value)
        assert self.value['msg']=='登录成功！'


if __name__ == '__main__':
    unittest.main(verbosity=2)