"""
===============
@author:Jack Mao
@time:2021-07-11 12:36
@e-mail:maol_5@163.com
===============
"""
import logging
import pytest
import yaml

def get_datas_div():
    #需要配置编码格式utf-8，否则会报错，UnicodeDecodeError
    with open("./datas/div_dates.yml",encoding="utf-8") as f:
        datas = yaml.safe_load(f)
    return datas

class TestDiv:
    @pytest.mark.parametrize("a,b,expect",get_datas_div()["datas"],
                             ids=get_datas_div()["ids"])
    def test_div(self,a,b,expect,get_calc_object_div,div_display):
        try:
            assert expect == get_calc_object_div.div(a, b)
        except ZeroDivisionError:
            logging.info("除数不能为0")
        except TypeError:
            logging.info("该数据类型不支持")