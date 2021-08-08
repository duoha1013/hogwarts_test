"""
===============
@author:Jack Mao
@time:2021-08-07 16:50
@e-mail:maol_5@163.com
===============
"""
import time

from task_pytest1.homework3.basepage import BasePage
from task_pytest1.homework3.memberpage import MemberPage


class AddressPage(BasePage):
    def goto_member_detail(self):
        time.sleep(15)
        #点击成员列表的某一个进入成员详情页面，以第二个为例
        self.driver.find_element_by_xpath('//*[@id="member_list"]/tr[2]').click()
        return MemberPage(self.driver)
