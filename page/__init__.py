from selenium.webdriver.common.by import By

"""此页面为tpshop商城登录的元素定位"""
login_link = (By.LINK_TEXT, '登录')  # 登录链接
username = (By.ID, 'username')  # 用户名
password = (By.ID, 'password')  # 密码
verify_code =( By.ID, 'verify_code')  # 验证码
login_sbtn = (By.NAME, 'sbtbutton')  # 登录按钮
