"""
===============
@author:Jack Mao
@time:2021-07-31 22:02
@e-mail:maol_5@163.com
===============
"""
from task_pytest1.homework3.officalpage import OfficalPage


class TestLogin:
    def setup(self):
        self.offical = OfficalPage()

    def test_login(self):
        #官网+登录+首页+通讯录+添加成员
        self.offical.goto_login_page().goto_first_page().goto_addmember_page().add_member("Rose",1020,13011122211)