"""
===============
@author:Jack Mao
@time:2021-07-31 22:03
@e-mail:maol_5@163.com
===============
"""
import time

import yaml

from task_pytest1.homework3.addmemberpage import AddMemberPage
from task_pytest1.homework3.memberpage import MemberPage
from task_pytest1.homework3.officalpage import OfficalPage
import pytest


def get_data():
    with open("data.yml", "r", encoding="utf-8") as f:
        data_var = yaml.safe_load(f)
    return data_var


class TestLogin:
    def setup_class(self):
        self.offical = OfficalPage()


    # @pytest.mark.parametrize("username,accoutid,phone", get_data()["datas"], ids=get_data()["ids"])
    # @pytest.mark.parametrize("username,accoutid,phone", [("a1", 1031, 13111222211), ("a2", 1032, 13111222213)])
    # def test_add_member(self, username, accoutid, phone):
    def test_add_member(self):
        # 官网+登录+首页+添加成员界面+成员数据
        self.offical.goto_login_page().goto_main_page().goto_addmember_page().add_member("a3", 1034, 13000111125)
        # 获取通讯录成员手机号码
        phone = MemberPage().get_member_phone()
        #断言手机号是否一致
        assert phone == "13000111125"
