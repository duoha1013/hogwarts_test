"""
===============
@author:Jack Mao
@time:2021-06-30:18:28
@e-mail:maol_5@163.com
===============
"""
"""
1.原有存款 1000元， 发工资之后存款变为 2000 元
2.定义发工资模块 send_money.py，用来增加收入计算
"""
import money
new_money = 0
flag = 0
def send():
    global new_money
    global flag
    new_money = 1000
    money.saved_money = money.saved_money + new_money
    print(f"已发放工资：{new_money}")
    flag = flag + 1



