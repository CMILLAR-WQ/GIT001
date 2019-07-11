import pytest
import os
import sys
sys.path.append(os.getcwd())

from tools.utils import UtilDriver
from page.page_login import PageLogin


# 参数
def get_data():
    return [("15100000001", "error", "8888"), ("15100001111", "123456", "8888"), ("15100000001", "123456", "8888")]


class TestLogin(object):
    def setup_class(self):
        self.login = PageLogin()
        self.driver = UtilDriver().get_driver()

    # 结束
    def teardown_class(self):
        # self.login.driver.quit()
        UtilDriver().quit_driver()

    def setup(self):
        self.driver.get('http://127.0.0.1/')

    @pytest.mark.parametrize("username,pwd,code", get_data())
    def test_login(self, username, pwd, code):
        self.login.page_login(username, pwd, code)
