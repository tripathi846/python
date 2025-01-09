# yield previus position or value ko hold kerke rekhta hai.


# def even_no(n):
#     i=2
#     while i<=n:
#         yield i
#         i=i+2
# n=int(input("enter your number"))
# data= even_no(n)
# print(data)
# data1= even_no(n)
# print(data1)

# ===================================================

def even_no(n):
    i=2
    while i<=n:
        yield i
        i=i+2
n=int(input("enter your number"))
# data= even_no(n)
# print(data)
data1= even_no(n)
print(next(data1))
print("hello")
        
