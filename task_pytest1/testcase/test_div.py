"""
===============
@author:Jack Mao
@time:2021-07-08:10:41
@e-mail:maol_5@163.com
===============
"""
import logging

import pytest
from task_pytest1.homework import calculator

class TestDiv:

    def setup_class(self):
        self.cal = calculator.Calculator()
        # print("除法测试开始")
        logging.info("除法测试开始")

    def teardown_class(self):
        # print("除法测试完成")
        logging.info("除法测试完成")

    def setup(self):
        logging.info("开始计算")

    def teardown(self):
        logging.info("结束计算")

    @pytest.mark.parametrize("a,b,expect",[(0,0,0),(1.0,2,0.5),(0,1,0),(0,2.0,0.0),(-2,-1,2),(2,-1,-2),
                                           (-2,1,-2),(-1.5,1.5,-1.0),(1.5,-1.5,-1.0),(2.5,2.5,1.0),(1.23,1.23,1.00),
                                           (-1.25,-1.25,1.00),(2.5,0,0),(-2.5,0,0),
                                           (True,False,0),(True,True,1.0),(False,False,0),(False,True,0.0),
                             ("1","1",0),("a","b",0),(1+1j,1+1j,1+0j),(1+1j,-1-1j,-1-0j),(-1-1j,-1-1j,1-0j),
                                           (1+1j,2,0.5+0.5j),(2,1+1j,1-1j),(-2,1+1j,-1+1j),(-2.5,1+1j,-1.25+1.25j),
                                               (1+1j,-2.5,-0.4-0.4j),(1+1j,2.5,0.4+0.4j),
                                           ("$",":",0),("."," ",0)],
                             ids=["整数0分母为0","小数与整数","分子为0的整数","分子为0的小数","负整数","正负整数除数为负整数",
                                  "正负整数分子为负","小数为正负数分母为正","小数为正负数分母为负","小数均为正","保留后2位的小数均为正",
                                  "保留后2位的小数均为负","分子为小数分母为0","分子为小数并为负分母为0",
                                  "布尔型T/F","布尔型T/T","布尔型F/F","布尔型F/T",
                                  "字符类型数字","字符类型字母","实部为正整数虚部为正的复数","除数为实部和虚部均为负的复数","分子分母均为实部虚部为负的复数",
                                  "分子为复数分母为正整数","分子为正整数分子为复数","分子为负整数分母为复数","分子为负的小数分母为复数",
                                  "分子为复数分母为负的小数","分子为复数分母为正的小数","特殊字符","特殊字符分母为空格"])
    def test_div(self,a,b,expect):
        if( type(b)==complex or (type(a) != str and type(b) != str and int(b) != 0)):
            assert expect == self.cal.div(a,b)
        elif(type(a) == str or type(b) == str ):
            # print("字符类型不支持除法运算")
            logging.info("字符类型不支持除法运算")
        elif(int(b) == 0):
            # print("除数为0，无法计算")
            logging.info("除数为0，无法计算")
            return 0
        else:
            # print("其他类型数据不支持除法运算")
            logging.info("其他类型数据不支持除法运算")
            return 0