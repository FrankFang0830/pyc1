# def my_abs(a):
#     if not isinstance(a,(int,float)):  #Check the type
#         raise TypeError("bad operand type")
#     if a>0:
#         return a;
#     if a<0:
# #         return -a;
#
#
# def power(x,n=2): #default argument
#     r=1
#     while n>0:
#         r=r*x
#         n=n-1
#     return r
# print(power(5, 3))

# def person(name, age, **kw):      #不管是什么只要后面有 就可以输出
#     print('name:', name, 'age:', age, 'other:', kw)
# person('f',18)
#
# def person(name, age, *, city, job): #只能输出City 和 job
#     print(name, age, city, job)
# person('f', 18, city='Beijing',job='a')

# def jie(n):
#     if n==1:
#         return 1
#     else:
#         return n*jie(n-1)
# print(jie(5))

class Student(object):

    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print('%s: %s' % (self.__name, self.__score))

    def get_name(self):
        print("your name is %s",self.__name)

    def set_score(self, score):
        if 0<score<100:
            self.__score = score
        else :
            raise ValueError('bad score')


student=Student("Fang",90)
student.print_score()
student.score=99
student._score=999
student.print_score()
student.get_name()
student.set_score(99999)
student.print_score()