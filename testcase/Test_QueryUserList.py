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

class QueryUserList(unittest.TestCase):

    def test_assert_ququeryUserList(self):
        headers = ('post', queryUserList_url, queryUserList_data, cms_headers)
        self.value = Test_Api.test_api(headers)
        assert self.value['msg'] == '查询用户成功！'

