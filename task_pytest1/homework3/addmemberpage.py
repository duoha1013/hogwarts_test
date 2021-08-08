"""
===============
@author:Jack Mao
@time:2021-07-31 22:00
@e-mail:maol_5@163.com
===============
"""
import time

from task_pytest1.homework3.basepage import BasePage


class AddMemberPage(BasePage):
    def add_member(self, username, accoutid, phone):
        # 调用父类元素定位封装方法，姓名、账号以及手机号
        BasePage.find_element(self, '//*[@id="username"]').send_keys(username)
        BasePage.find_element(self, '//*[@id="memberAdd_acctid"]').send_keys(accoutid)
        BasePage.find_element(self, '//*[@id="memberAdd_phone"]').send_keys(phone)
        time.sleep(2)
        BasePage.find_element(self, '//*[@class="js_member_editor_form"]/div[1]/a[1]').click()

