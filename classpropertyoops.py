# using parent class
# class p:
#     def __init__(self,p_name):
#         self.x=p_name
#     def p_properties(self,home,bank):
#         self.h=home
#         self.b=bank
# class c(p):
#     def c_property(self,quali):
#         self.q=quali
#         print(self.h)
#         print(self.b)
#         print(self.q)
#         print(self.x)
# obj=c("shivansh")
# # obj.p_properties("narmadapuram","icici")
# # obj.c_property("b.com")
# print(dir(c))
# print(dir(obj))
# ====================using child class==============================
# class p:
#     def __init__(self,p_name):
#         self.x=p_name
#     def p_properties(self,home,bank):
#         self.h=home
#         self.b=bank
#         print(self.h)
#         print(self.b)

# class c(p):
#     def c_property(self,quali):
#         self.q=quali
#         self.p_properties("narmadapuram","hdfc")
#         print(self.q)
#         print(self.x)
# obj=c("shivansh")
# # obj.p_properties("narmadapuram","icici")
# obj.c_property("b.com")
# ===========================multilable inheritance================
# class gf:
#     def name(self,name):
#         self.n=name
  
# class p(gf):
#     def __init__(self,p_name):
#         self.x=p_name
#     def p_properties(self,home,bank):
#         self.h=home
#         self.b=bank
#         print(self.h)
#         print(self.b)
        
# class c(p):
#     def c_property(self,quali):
#         self.q=quali
#         self.p_properties("narmadapuram","hdfc")
#         print(self.q)
#         print(self.x)
#         self.name("shivansh tripathi")
#         print(self.n)
# obj=c("shivansh")
# obj.c_property("b.com")



# ex2==

# class gf:
#     def name(self,name):
#         self.x=name
# class f(gf):
#     def f_name(self,f_name):
#         self.y=f_name
# class c(f):
#     def c_name(self,c_name):
#         self.z=c_name
# obj=c()
# obj.name("cybrom")
# =========================multiple===================================
# class father:
#     x=10
#     def property(self):
#         self.name="f_name"
#         self.bank="f_bank"
#         print(self.name,self.bank)
# class mother:
#     y=20
#     def property(self):
#         self.name="m_name"
#         self.bank="m_bank"
#         print(self.name,self.bank)

# class son(father,mother):
#     pass
# obj =son()
# obj.property()
# # print(dir(son))