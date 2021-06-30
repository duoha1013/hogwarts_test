"""
===============
@author:Jack Mao
@time:2021-06-30:18:29
@e-mail:maol_5@163.com
===============
"""
import select_money
import send_money
"""
1.原有存款 1000元， 发工资之后存款变为 2000 元
2.定义模块 money.py，模块中定义 saved_money = 1000
3.定义发工资模块 send_money.py，用来增加收入计算
4.定义工资查询模块 select_money.py，用来展示工资数额
5.定义一个 start.py，启动文件展示最终存款金额
"""

if __name__ == '__main__':
    send_money.send()
    send_money.send()
    send_money.send()
    send_money.send()
    select_money.select()
