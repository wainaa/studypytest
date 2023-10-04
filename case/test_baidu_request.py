import re

import pytest
import requests

from Test_demo.login import login
from utils.read_data import load_yaml_data


@pytest.mark.初学pytest
class TestStudy:
    session = requests.session()

    # def setup_method(self):
    #     print("方法初始化")
    #
    # def teardown_method(self):
    #     print("方法结束")
    #
    # @classmethod
    # def setup_class(cls):
    #     print("类初始化")
    #
    # @classmethod
    # def teardown_class(cls):
    #     print("类结束")

    @pytest.mark.parametrize('params', load_yaml_data('baiduRequest'))
    def test_baidu_001(self, setup, params):
        url = params['url']
        rep = TestStudy.session.request(params['method'], url)
        res = re.search('name=(.*?) class=bri', rep.text)[1]
        print("001")
        assert 'tj_briicon' == res

    @pytest.mark.parametrize('params', load_yaml_data('guishudiRequest'))
    def test_baidu_002(self, params):
        url = params['url']
        rep = TestStudy.session.request(params['method'], url, json=params['params'])
        assert rep.status_code == 200

    @pytest.mark.parametrize("user", load_yaml_data('userinfo'))
    def test_baidu_003(self, setup, user):
        isexpect = login(user['username'], user['password'])
        assert isexpect == user['expect']

    @pytest.mark.parametrize("user", load_yaml_data('123'))
    def test_baidu_004(self, setup, user):
        print(user)

    @pytest.mark.parametrize("params", load_yaml_data('shoujiRequest'))
    def test_mobile(self, params):
        res = TestStudy.session.request(params['method'], url=params['url'], data=params['params'])
        assert res.status_code == 200
