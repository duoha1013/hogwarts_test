"""
===============
@author:Jack Mao
@time:2021-07-11 12:35
@e-mail:maol_5@163.com
===============
"""
import logging

import pytest
import yaml

def get_datas():
    with open("./datas/add_dates.yml",encoding='utf-8') as f:
        datas = yaml.safe_load(f)
    return datas

class TestAdd:

    @pytest.mark.parametrize("a,b,expect",get_datas()["datas"],
                             ids=get_datas()["ids"])
    #add_display显示调用，若隐性调用可在conftest中将fixture关键字参数配置成autouse=True
    def test_add(self,a,b,expect,get_calc_object,add_display):
        #将复数类型单独拎出来，否则跟字符串类型一样进行拼接
        if ("j" in str(a)) and ("j" in str(b)):
            a = complex(a)
            b = complex(b)
            expect = complex(expect)
            assert expect == get_calc_object.add(a,b)
        #将小数正负0.3表示的特殊情况单独拉出来断言
        elif(0.1==a and 0.2==b) or (0.2==a and 0.1 == b) or (-0.1==a and -0.2==b) or (-0.2==a and -0.1==b):
            assert round(expect,4) == round(get_calc_object.add(a, b),4)
        else:
            assert expect == get_calc_object.add(a, b)
