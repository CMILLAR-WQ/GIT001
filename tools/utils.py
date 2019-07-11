"""公共方法类"""
from time import sleep
from selenium import webdriver


class UtilDriver(object):
    # 获取浏览器驱动对象
    driver = None

    @classmethod
    def get_driver(cls):
        if not cls.driver:
            cls.driver = webdriver.Chrome()
            cls.driver.get("http://127.0.0.1/")
            cls.driver.maximize_window()
            cls.driver.implicitly_wait(10)
        return cls.driver

    # 关闭浏览器驱动对象
    @classmethod
    def quit_driver(cls):
        if cls.driver:
            sleep(3)
            cls.driver.quit()
            cls.driver = None



