#mulatipal attrubute,multipal methods ko combine kerke rap kerna he encapsulation hota hai

# class a:
#     x=10
#     def __init__(self,name):
#         self.name=name
#     @classmethod
#     def show(cls,age):
#         cls.age=age
#     @staticmethod
#     def display(school):
#         print(school)

#acess speciiers:- 
# 1.public(govt.place)
# 2.protected(covered campus)
# 3.private(private house)


# 2.protected(covered campus)=
class a:
    __x=10 #protected  class variable
    def __show(self):# protected instance variable
        print("from class a")
class b(a):
     pass

print(dir(b))
obj=b()
print(obj._a__x)
obj._a__show()