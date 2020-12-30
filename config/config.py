"""
======================
@author:多测师-黄sir
@time:2020/12/20:10:01
@email:hw18983616870@163.com
======================
"""
'''此模块用来存放所有接口的配置参数信息'''
cms_headers = {"Content-Type":"application/x-www-form-urlencoded"}
# 1.登录接口的参数信息
login_url = 'http://cms.duoceshi.cn/cms/manage/loginJump.do'
login_data = {
                    "userAccount":"admin",
                    "loginPwd":123456
                }

# 2.用户查询接口的参数信息
queryUserList_url = 'http://cms.duoceshi.cn/cms/manage/queryUserList.do'
queryUserList_data = {
    'startCreateDate': '',
    'endCreateDate': '',
    'searchValue': '',
    'page': 1
}
