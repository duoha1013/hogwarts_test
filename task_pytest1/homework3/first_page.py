"""
===============
@author:Jack Mao
@time:2021-08-02 17:35
@e-mail:maol_5@163.com
===============
"""

from task_pytest1.homework3.addmemberpage import AddMemberPage
from task_pytest1.homework3.addresspage import AddressPage
from task_pytest1.homework3.basepage import BasePage


class FirstPage(BasePage):
    def goto_addmember_page(self):
        # 从首页点击“添加成员”跳转到添加成员界面，采用return返回
        self.driver.find_element_by_xpath('//*[@class="index_service_cnt js_service_list"]/a[1]//span[2]').click()
        return AddMemberPage(self.driver)

    def goto_address_page(self):
        # 从首页进入通讯录页面，将driver传递给通讯录页面
        self.driver.find_element_by_xpath('//*[@id="menu_contacts"]').click()
        return AddressPage(self.driver)

