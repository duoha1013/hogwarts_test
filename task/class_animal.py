"""
===============
@author:Jack Mao
@time:2021-07-04:11:49
@e-mail:maol_5@163.com
===============
"""
"""
1.写一个面向对象的例子：
比如创建一个类（Animal）【动物类】，类里有属性（名称，颜色，年龄，性别），类方法（会叫，会跑）
创建子类【猫】，继承【动物类】
重写父类的__init__方法，继承父类的属性
添加一个新的属性，毛发=短毛
添加一个新的方法， 会捉老鼠，
重写父类的‘【会叫】的方法，改成【喵喵叫】
创建子类【狗】，继承【动物类】
复写父类的__init__方法，继承父类的属性
添加一个新的属性，毛发=长毛
添加一个新的方法， 会看家
复写父类的【会叫】的方法，改成【汪汪叫】

2.在入口函数中创建类的实例
创建一个猫猫实例
调用捉老鼠的方法
打印【猫猫的姓名，颜色，年龄，性别，毛发，捉到了老鼠】
创建一个狗狗实例
调用【会看家】的方法
打印【狗狗的姓名，颜色，年龄，性别，毛发】
"""

class Animal:
    def __init__(self,name,color,age,gender):
        self.name = name
        self.color = color
        self.age = age
        self.gender = gender

    def animal_calls(self):
        print("叫声很大")

    def animal_run(self):
        print("跑得挺快")


class Cat(Animal):
    def __init__(self,name,color,age,gender,hair):
        self.hair = hair
        super().__init__(name,color,age,gender)

    def animal_calls(self):
        print("喵喵喵")

    def catch_mice(self):
        print(f"猫猫的姓名【{self.name}】，颜色【{self.color}】，年龄【{self.age}】，性别【{self.gender}】，毛发【{self.hair}】，捉到了老鼠")

class Dog(Animal):
    def __init__(self,name,color,age,gender,hair):
        self.hair = hair
        super().__init__(name,color,age,gender)

    def look_house(self):
        print("我会看家")
        print(f"狗狗的姓名【{self.name}】，颜色【{self.color}】，年龄【{self.age}】，性别【{self.gender}】，毛发【{self.hair}】")

    def animal_calls(self):
        print("汪汪汪")


if __name__ == '__main__':

    cat1 = Cat("汤姆","黑色","0.5岁","雄性","短毛")
    cat1.catch_mice()

    dog1 = Dog("莱福","棕色","1岁","雌性","短毛")
    dog1.look_house()
