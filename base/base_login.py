from selenium.webdriver.support.wait import WebDriverWait

from tools.utils import UtilDriver


class BaseLogin(object):
    # 初始化实例对象
    def __init__(self):
        self.driver = UtilDriver().get_driver()

    def base_find_element(self, loc, timeout=10, poll=0.2):
        """元素的定位方法"""
        return WebDriverWait(self.driver, timeout=timeout, poll_frequency=poll).until(
            lambda x: x.find_element(*loc))
    def base_input(self,el,data):
        #输入内容的操作方法
        element=self.base_find_element(el)
        element.clear()
        element.send_keys(data)
    def base_click(self,el):
        #点击的操作方法
        self.base_find_element(el).click()

