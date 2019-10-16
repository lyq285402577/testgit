#！/usr/bin/python
#-*-coding:utf-8-*-
# class Lei():
#     pass
# Lei()

# class Cat():
#     #属性
#     def __init__(self,newweiba,newcolor):
#         self.weiba = newweiba
#         self.color = newcolor
#     def __str__(self):
#         msg = '有没有尾巴:'+self.weiba+'\n颜色:'+self.color
#         return msg
#     #方法
#     def __eat(self):
#         print('-----吃-----')
#         return 1
#     def drink(self):
#         print('-----喝-----')
# xiaohuamao = Cat('有','花色')
# print(xiaohuamao)
# xiaobaimao = Cat('没有','白色')
# print(xiaobaimao)
    # def prinfo(self):
    #     print(self.color)
    #     print(self.weba)
    #     print(self.__eat())

#多态
# class Animal():     #统一形态
#     def talk(self):
#         pass
# class People(Animal):   #动物的第一个形态：人
#     def talk(self):
#         print('say hello')
# class Pig(Animal):      #动物的第二个形态：猪
#     def talk(self):
#         print('hengheng')
# class Dog(Animal):      #动物的第三个形态：狗
#     def talk(self):
#         print('wangwang')
#
# People().talk()
# Dog().talk()

#方法重写
class Student:
    def hanshu(self):
        print('nihao')
class KdStudent(Student):
    def hanshu(self):
        print('sahisuhisf2')
laowang = KdStudent()
laowang.hanshu()




