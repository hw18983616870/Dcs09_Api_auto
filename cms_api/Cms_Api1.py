# from config.config import *
# import requests
# session = requests.Session()

class Test_Api:
    '''设置一个session对象，以单例模式的写法。用于保持会话状态'''
    @classmethod
    def set_session(cls,session):
        cls.session = session

    @classmethod
    def get_session(cls):
        return cls.session

    @classmethod
    def test_api(cls,headers):
        # headers = ('post', login_url, login_data, cms_headers)
        response = cls.session.request(method=headers[0],url=headers[1],data=headers[2],headers=headers[3])
        return response.json()
        # print(response.json())
# if __name__ == '__main__':
    # t =Test_Api()
    # t.set_session(session)
    # t.get_session()
    # headers = ('post', login_url, login_data, cms_headers)
    # t.test_api(headers)