"""
===============
@author:Jack Mao
@time:2021-07-31 21:58
@e-mail:maol_5@163.com
===============
"""
from task_pytest1.homework3.basepage import BasePage
from task_pytest1.homework3.loginpage import LoginPage


class OfficalPage(BasePage):
    def goto_login_page(self):
        # 官网进入登录页面，点击企业登录，并把登录界面return返回
        self.driver.find_element_by_xpath('//*[@id="indexTop"]/div[2]/aside/a[1]').click()
        return LoginPage(self.driver)
