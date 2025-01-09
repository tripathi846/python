# class syntex===
# class student:
#     "student information"
#     name="shivansh tripathi"
#     age=21
#     def add(p,q):
#         return p+q
# # print(dir(student))
# # print(student.__doc__)
# # print(student.__dict__)

# obj=student
# print(obj.name)
# print(obj.age)
# x = obj.add(5,9)
# print(x)

# =====================================================

# class student:
#     "student information"
#     name="shivansh tripathi"
#     age=21
#     def __init__(x):
#         print(id(x))
#         print("constructor called.....")
#     def add(p,q):
#         return p+q
# obj =student()
# print(id(obj))

# ==========================================================

# class student:
#     "student information"
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#     def show_detail(self):
#         print(self.name)
#         print(self.age)

# obj =student("shivansh",21)
# obj.show_detail()

# obj1 =student("abhay",25)
# obj1.show_detail()

# ====================

# compile declaraction==

# class student:
#     def __init__(self,name,age): #declaration
#         self.name=name    #declaration
#         self.age=age        #calling
#         print(self.name)
#     def add(self,school):
#         self.school=school   #dec
#     def show_detail(self):
#         print(self.name)     #calling
#         print(self.age)      #calling
#         print(self.school)   #calling
#         print(self.city)     #calling
# obj=student("shivansh",21)
# obj.add('shsc')
# print(obj.name)              #calling
# obj.city="narmadapuram"
# obj.show_detail()
#  instance variable over---
# =======================================

# static variable /class variable =
# declaring==

# class student:
#     school='shsc'
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
#         student.city='NARMADAPURAM'
#     def add_detail(self):
#         student.school_code=101

# obj=student('shivansh tripathi',21)
# student.principal="boss"

# calling==


# class Student:
#     "Student Information"
#     school = "SHSC"                         # declaration of static variable in side class but outside of the mehtod.......
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#         Student.city = "NARMADAPURAM"             # declaration of static variable inside constrctor.......
#         print("Calling inside of Constructor = ",Student.school)               # calling of static variable.......
#     def add_detail(self):
#         Student.school_code=101             # declaration of static variable inside instance method.......
#         print("Calling inside of instance method = ",Student.school)               # calling of static variable.......
#         print("Calling inside of instance method = ",Student.city)                 # calling of static variable.......
#     def show_detail(self):
#         print(Student.school)
#         print(Student.city)
#         print(Student.school_code)
#         print("Calling inside of instance method = ",Student.principal)
        
# obj = Student("shivansh",21)
# print("My_City=",Student.city)
# print("My_School=",Student.school)
# obj.add_detail()
# print("School_code=",Student.school_code)
# Student.principal = "Indra Bahadur"        # declaration of static variable.......
# obj.show_detail()



# local variable=

# x=50              #global
# class student:
#     global x
#     x=10
#     def add():
#         print(x)   #local
#         z=20
#         print(z)
#     def add1():
#         print(x)
# obj=student
# obj.add()
# obj.add1()
# print(x)
# =====================example=========================
# x=10
# class cybrom:
#     global x
#     x=50
#     def add():
#         print(x)
#         z=100
#         print(z)
#     def add1():
#         print(x)
# obj=cybrom
# obj.add()
# obj.add1()
# print(x)
# =================================================
# x=50
# def new():
#    global x
#    print(x)
#    x=10
#    print(x)

# print(x)
# new()
# print(x)

# ==========================+================

# methods:=
# 1.instance method 

# class a:
#     def new(self):              #declaration
#         print("1st method")
#     def new1(self):              #calling
#         self.new()
#         print("2st method")
# obj=a()
# obj.new()
# obj.new1()
# ==========================+================
# 2.class method= static variable ke value ke modify kerne ke liyea hum class ka use kerte hi


class book:
    price=150
    def __init__(self,author,pages):
        self.author=author
        self.pages=pages
    @classmethod
    def update_price(cls,price):
        cls.price=price
    def show_details(self):
        print(self.author)
        print(book.price)
        print(self.pages)

obj=book('shiavnsh',100)
obj.show_details()
obj.update_price(200)
obj.show_details()























