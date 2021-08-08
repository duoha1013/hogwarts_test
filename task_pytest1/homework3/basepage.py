"""
===============
@author:Jack Mao
@time:2021-07-31 21:58
@e-mail:maol_5@163.com
===============
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class BasePage:
    URL = "https://work.weixin.qq.com/"
    def __init__(self, driver: webdriver = None):
        # 基类页面初始化，webdriver只需要实例化一次，后续跳转页面无需再次实例化
        # if not driver:
        #     self.driver = webdriver.Chrome()
        #     self.driver.get("https://work.weixin.qq.com/")
        # else:
        #     self.driver = driver
        if not driver:
            option = Options()  #复用浏览器来调试
            option.debugger_address = "localhost:9222"
            self.driver = webdriver.Chrome(options=option)
            self.driver.get(self.URL)
        else:
            self.driver = driver

    def find_element(self, xpath):
        # 封装元素定位方法，使用xpath方式，简单易用
        time.sleep(2)
        return self.driver.find_element_by_xpath(xpath)

