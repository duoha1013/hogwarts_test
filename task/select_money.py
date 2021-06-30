"""
===============
@author:Jack Mao
@time:2021-06-30:18:28
@e-mail:maol_5@163.com
===============
"""
"""
定义工资查询模块 select_money.py，用来展示工资数额
"""
import money
import send_money
def select():
    print(f"工资额为：{send_money.new_money},共发放了{send_money.flag}次")
    print(f"最终存款金额为：{money.saved_money}")