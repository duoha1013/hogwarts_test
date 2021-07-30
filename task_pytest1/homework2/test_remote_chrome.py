"""
===============
@author:Jack Mao
@time:2021-07-28 11:33
@e-mail:maol_5@163.com
===============
"""
import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestSelenium:
    def test_reuse_chrome(self):
        #复用浏览器方式，企业微信扫描二维码只需要一次即可，方便调试
        #步骤1：实例化option
        option = Options()
        #步骤2：配置本地地址及端口号
        option.debugger_address = "localhost:9222"
        #步骤3：实例化chrome driver,把option传入进去
        self.driver = webdriver.Chrome(options=option)
        #步骤4：传入待测网址https://work.weixin.qq.com/wework_admin/loginpage_wx?
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        time.sleep(5)

        #使用css_selector方式查找“添加成员”元素，并进行点击
        self.driver.find_element_by_css_selector("#_hmt_click > div.index_colLeft > div.index_service > div.index_service_cnt.js_service_list > a:nth-child(1) > div").click()
        #跳转页面需要等待时间，不然下一步定位元素会找不到，报错
        time.sleep(10)
        #步骤5：用xpath方式查找姓名、账号、手机号元素，并进行send_keys发送符合规则的数据信息
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys("Jimmy")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys("1013")
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys("13712122121")
        #步骤6：点击“保存并继续添加”，用xpath方式元素定位
        self.driver.find_element_by_xpath('//*[@id="js_contacts45"]/div/div[2]/div/div[4]/div/form/div[1]/a[1]').click()
        time.sleep(3)

        self.driver.quit()