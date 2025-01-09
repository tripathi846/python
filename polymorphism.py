
# =====================overloading===========================
# class a:
#     def add (self,x,y):
#         return x+y
#     def add (self,x,y,z):
#         return x+y+z
# obj=a()
# obj.add(10,20)

# ======
# class a:
#     def add(self,*n):
#         sum=0
#         for i in n:
#             sum=sum+i
#         return sum
# obj=a()
# x=obj.add(10,20)
# print(x)
# y=obj.add(10,20,30)
# print(y)
# =====================overriding===========================
class a:
    def display(self):
        print("from class a")

class b(a):
    def display(self):
        print("from class b")
    def p_display(self):
        self.display()
        super().display()   #direct parent ke  method ko call kerne ke liyea hum super ride ka use kerte hai
obj=b()
obj.p_display()
obj.display()