"""
===============
@author:Jack Mao
@time:2021-08-07 18:18
@e-mail:maol_5@163.com
===============
"""
import time

from task_pytest1.homework3.basepage import BasePage

class MemberPage(BasePage):
    url = "https://work.weixin.qq.com/wework_admin/frame#contacts"
    def window_driver(self):
        #进入通讯录页面
        self.driver.get(self.url)
        self.find_element('//*[@id="menu_contacts"]/span').click()
        time.sleep(5)
        #进入通讯录的成员列表页面，url是一样的
        self.find_element('//*[@id="member_list"]/tr[2]').click()


    def get_member_name(self):
        self.window_driver()
        time.sleep(5)
        #获取成员的姓名属性值
        return self.driver.find_element_by_xpath('//*[@class="member_display_cover_detail_name"]').text

    def get_member_accountid(self):
        self.window_driver()
        time.sleep(5)
        #获取成员详情的账号
        return self.driver.find_element_by_xpath('//*[@class="member_display_cover_detail_bottom"][1]').text

    def get_member_phone(self):
        self.window_driver()
        time.sleep(5)
        #获取成员详情的手机号
        phone = self.driver.find_element_by_xpath(
            '//*[@class="member_display_item member_display_item_Phone"]/div[2]').text
        return phone
