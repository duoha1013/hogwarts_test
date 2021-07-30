"""
===============
@author:Jack Mao
@time:2021-07-28 11:34
@e-mail:maol_5@163.com
===============
"""
import time
import yaml
from selenium import webdriver


class TestSelenium:
    def test_get_cookie(self):
        # 步骤1：实例化浏览器句柄driver
        self.driver = webdriver.Chrome()
        # 步骤2：传入待测企业微信网址https://work.weixin.qq.com/wework_admin/loginpage_wx?
        self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
        # 步骤3：等待20s用于扫二维码进行登录
        time.sleep(20)
        # 步骤4：获取cookie，相当于拿了一把进门的钥匙，为后续免登录
        cookie_var = self.driver.get_cookies()
        # 步骤5：将cookie_var保存到yaml文件中，以备后续调用
        yaml.safe_dump(cookie_var, open("cookie.yml", "w", encoding="utf-8"))
        time.sleep(5)

    def test_add_cookie(self):
        # 步骤1：打开浏览器，输入企业网址，清除所有的cookie
        self.driver = webdriver.Chrome()
        self.driver.get("https://work.weixin.qq.com/wework_admin/frame")
        self.driver.delete_all_cookies()
        # 步骤2：从yaml文件中加载cookie
        cookie_var = yaml.safe_load(open("cookie.yml", "r", encoding="utf-8"))
        for cookie in cookie_var:
            self.driver.add_cookie(cookie)
            print(cookie)
        # 写入cookie需要时间
        time.sleep(10)
        # 步骤3：需要刷新下页面才可以进去
        self.driver.refresh()
        time.sleep(5)

        # 步骤4：点击首页中的添加成员，跳转到通讯录添加成员页面
        self.driver.find_element_by_xpath('//*[@id="_hmt_click"]/div[1]/div[4]/div[2]/a[1]/div/span[2]').click()
        time.sleep(5)
        # 步骤5：定位姓名、账号、手机号，输入符合规则的数据
        self.driver.find_element_by_xpath('//*[@id="username"]').send_keys('Tommy')
        self.driver.find_element_by_xpath('//*[@id="memberAdd_acctid"]').send_keys(1015)
        self.driver.find_element_by_xpath('//*[@id="memberAdd_phone"]').send_keys(13000001111)
        self.driver.find_element_by_xpath('//*[@id="js_contacts45"]/div/div[2]/div/div[4]/div/form/div[1]/a[1]').click()
        time.sleep(2)
        self.driver.quit()
