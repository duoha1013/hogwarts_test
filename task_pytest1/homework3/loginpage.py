"""
===============
@author:Jack Mao
@time:2021-07-31 21:59
@e-mail:maol_5@163.com
===============
"""
import os
import time
import yaml

from task_pytest1.homework3.basepage import BasePage
from task_pytest1.homework3.first_page import FirstPage


class LoginPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame"
    def get_cookie_to_file(self):
        # 获取cookie
        cookie_var = self.driver.get_cookies()
        # 将cookie_var保存到yaml文件中，以备后续调用
        yaml.safe_dump(cookie_var, open("cookie.yml", "w", encoding="utf-8"))
        time.sleep(5)

    def load_cookie(self):
        # 从cookie.yml文件读取cookie，需要for循环进行写入
        cookie_var = yaml.safe_load(open("cookie.yml", "r", encoding="utf-8"))
        for cookie in cookie_var:
            self.driver.add_cookie(cookie)
        # 写入cookie需要时间
        time.sleep(10)
        # 需要刷新下页面才可以进去
        self.driver.get(LoginPage.url)
        time.sleep(5)

    def scan_code(self):
        # 判断是否有cookie.yml文件，没有就调用get_cookie_to_file获取cookie，否则直接读取已有cookie进行写入
        if not os.path.exists("cookie.yml"):
            LoginPage.get_cookie_to_file(self)
        else:
            LoginPage.load_cookie(self)

    def goto_first_page(self):
        # 采用的是cookie方式
        # 跳转至首页，需要登录扫码加载cookie并进行写入操作，然后return返回登录后的首页
        LoginPage.scan_code(self)
        time.sleep(5)
        return FirstPage(self.driver)

    def goto_main_page(self): #采用复用浏览器的方式进入首页，只需第一次扫码后直接更新首页的url
        time.sleep(5)
        self.driver.get(LoginPage.url)
        return FirstPage(self.driver)

    def register(self):
        pass
