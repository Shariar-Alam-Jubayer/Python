# class Account :

#     def __init__(self,acc_no,acc_pass) :
#         self.acc=acc_no
#         self.__acc_pass=acc_pass

#     def reset_pass(self):
#         print(self.__acc_pass)



# acc1=Account(127321,12345)
# print(acc1.acc)
# print(acc1.reset_pass())

# class Person:
#     __name="amu"
#     def __hello(self):
#         print("welcome miss")

#     def welcome(self):
#         print(self.__hello())


# s1=Person()
# s1.welcome()

# inheritance using super mathod
# class Car :
#     coler="blue"
#     def __init__(self,type):
#         self.type=type

#     @staticmethod
#     def start():
#         print("car started")
    
#     @staticmethod
#     def stop():
#         print("car stopped")
    
# class tata(Car):
#     def __init__(self,name,type):
#         super().__init__(type)
#         # super().start()
#         self.name=name
#         super().start() 
        
# car1=tata("Aliean","electric")
# print(car1.type)
# print(car1.coler)
# # car1.start()
# # car1.stop()

##class method
# class Person:
#     name="jubayer"

#     # def changename(self,name):
#     #     self.__class__.name="m"
#     @classmethod
#     def changename(cls,name):
#         cls.name=name

# p1=Person()
# p1.changename("muniya")
# print(p1.name)
# print(Person.name)

##property

class Student:
    def __init__ (self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
    @property
    def percentage(self):
        return str((self.phy + self.chem + self.math) / 3)+"%"

s1=Student(98,97,99)
print(s1.percentage)

s1.phy=86
print(s1.percentage)



