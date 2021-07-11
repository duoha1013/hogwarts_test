"""
===============
@author:Jack Mao
@time:2021-07-11 12:42
@e-mail:maol_5@163.com
===============
"""
import logging
import pytest
from task_pytest1.homework import calculator

#默认fixture：scope="function"  函数级，相当于setup,teardown
@pytest.fixture()
def add_display():
    logging.info("开始计算")
    yield
    logging.info("结束计算")

#设置fixture：scope="class"  类级，相当于setup_class,teardown_class
#获取Calculator()实例对象
@pytest.fixture(scope="class")
def get_calc_object():
    calc = calculator.Calculator()
    logging.info("加法测试开始")
    yield calc
    logging.info("加法测试完成")

#除法测试fixture设置，区别加法，相当于setup_class/teardown_class
@pytest.fixture(scope="class")
def get_calc_object_div():
    calc = calculator.Calculator()
    logging.info("除法测试开始")
    yield calc
    logging.info("除法测试完成")

#除法测试fixture设置，区别加法，相当于setup/teardown
@pytest.fixture()
def div_display():
    logging.info("开始计算")
    yield
    logging.info("结束计算")

#修改编码格式，可以让它在用例显示中文
def pytest_collection_modifyitems(session, config, items:list):
    # print(items)
  for item in items:
      item.name = item.name.encode('utf-8').decode('unicode-escape')
      item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')