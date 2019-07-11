import page
from base.base_login import BaseLogin


class PageLogin(BaseLogin):

    def page_click_login_link(self):
        # 点击登录链接
        self.base_click(page.login_link)

    def page_input_username(self, username):
        # 输入用户名
        self.base_input(page.username, username)

    def page_input_password(self, pwd):
        # 输入密码
        self.base_input(page.password, pwd)

    def page_input_code(self, code):
        # 输入验证码
        self.base_input(page.verify_code, code)

    def page_click_login_btn(self):
        # 点击登录按钮
        self.base_click(page.login_sbtn)

    # 实现登录的业务层操作
    def page_login(self, username, pwd, code):
        self.page_click_login_link()  # 点击登录链接
        self.page_input_username(username)  # 输入用户名
        self.page_input_password(pwd)  # 输入密码
        self.page_input_code(code)  # 输入验证码
        self.page_click_login_btn()  # 点击登录
