#！/usr/bin/python
#-*-coding:utf-8-*-
#继承
class Student:
    def __init__(self):
        self.name = '空的'
    def hanshu(self):
        print(120)
    def hanshu1(self):
        print(110)
class KdStudent(Student):
    pass
laowang = KdStudent()
laowang.hanshu()
laowang.hanshu1()


#多继承
class Student:
    def __init__(self):
        self.name = '空的'
    def hanshu(self):
        print(120)
    def hanshu1(self):
        print(110)
class Yuangong:
    def __init__(self):
        self.home = '地区'
    def diqu(self):
        print('河南')
    def hanshu(self):
        print('北京')
class KdStudent(Student,Yuangong):
    pass
laowang = KdStudent()
laowang.hanshu()
laowang.hanshu1()
laowang.diqu()
laowang.hanshu()



