"""
poly-morphism
many-form

types:
1. method overloading
2. method overriding
"""
# list = [2,3,4,56,5]
# print(len(list))
# a = "welcome"
# print(len(a))

# class info:
#     # constructor
#     def __init__(self, name=" "):
#         print('from constructor', name)
# a = info()
# a = info("rahul")
# a.__init__()

# method overloading
"""
-> within the same class
-> same method name
-> different parameter
"""
# class info:
#     def __init__(self):
#         print("something goes here")
#     def displayInfo(self):
#         print('no arguments')

#     def displayInfo(self, name=''):
#         print("from name argument", name)

#     def displayInfo(self, name='', role=''):
#         print("from name and role arguments", name, role)

# obj = info()
# obj.displayInfo()
# obj.displayInfo("rahul")
# obj.displayInfo("suman", "admin")

# method overriding
"""
-> different class
-> same function
-> same parameter
"""

# class A:
#     def info(self, name=''):
#         print('from class A')

# class B(A):
#     def info(self, name=''):
#         super().info() # to call the parent class method
#         print('from class B', name) 

# a = A()
# # a.info()
# b = B()
# b.info('rahul')

class A:
    def info(self):
        print('class A')

class B:
    def info(self):
        print('class B')

a = A()
b = B()

def displayInfo(param):
    param.info()

displayInfo(b)
