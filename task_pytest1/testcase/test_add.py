"""
===============
@author:Jack Mao
@time:2021-07-08:10:40
@e-mail:maol_5@163.com
===============
"""
import logging
import allure
import pytest
from task_pytest1.homework import calculator

@allure.feature("加法")
class TestAdd:

    def setup_class(self):
        self.cal = calculator.Calculator()
        # print("加法测试开始")
        logging.info("加法测试开始")

    def teardown_class(self):
        # print("加法测试完成")
        logging.info("加法测试完成")

    def setup(self):
        # print("开始计算")
        logging.info("开始计算")

    def teardown(self):
        # print("结束计算")
        logging.info("结束计算")

    @pytest.mark.parametrize("a,b,expect",[(0,0,0),(1.0,2,3.0),(-1,1,0),(2,3,5),(-2,-3,-5),(0.5,0.5,1.0),
                                           (0.25,2.46,2.71),(-1.52,1.52,0.00),(2.3+1j,3.2+2j,5.5+3j),
                                           (-2+1j,2+2j,3j),(-1.5+1j,1.5+1j,0+2j),(1+1j,-1-1j,0),
                                           (True,False,1),(True,True,2),(False,False,0),
                                           ("1","1","11"),("a","b","ab"),("-1.0","1.0","-1.01.0"),
                                           ("__","#$#","__#$#"),("wafd","  中国","wafd  中国")],
                             ids=["整数0","小数与整数","正负整数","正整数","负整数","小数",
                                  "小数点两位","小数与绝对小数","小数为实部的复数","实部为正负整数的复数","实部为绝对小数的复数","相加为0的复数",
                                  "布尔型T+F","布尔型T+T","布尔型F+F","字符类型数字","字符类型字母","字符类型浮点数","特殊字符","特殊字符含中文和空格"])
    def test_add(self,a,b,expect):
        assert expect == self.cal.add(a,b)