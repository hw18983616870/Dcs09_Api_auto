"""
======================
@author:多测师-黄sir
@time:2020/12/20:11:44
@email:hw18983616870@163.com
======================
"""
import unittest
from utlis.HTMLTestRunner3_New import HTMLTestRunner
from utlis.mail3 import SendMail
import time
def run_all():
    test_path = r'D:\workspace\Dcs09_Api_auto\testcase'
    path = r'D:\workspace\Dcs09_Api_auto\report'
    now = time.strftime('%Y-%m-%d-%H-%M-%S')
    filename = path+'\\'+str(now)+'_api_report.html'
    f = open(file=filename,mode='wb')
    discover = unittest.defaultTestLoader.discover(start_dir=test_path,pattern='Test*.py')
    runner = HTMLTestRunner(stream=f,
                            title='CMS平台接口测试用例报告',
                            description='接口测试用例执行情况：',
                            tester='dcs_xiaohuang')
    runner.run(discover)
    f.close()
    sendmail = SendMail(send_msg=filename,attachment=filename)
    sendmail.send_mail()

run_all()