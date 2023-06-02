# single level inheritance
class A:
    name = "ram"
    age = 15
    id = 1

    def demo(self):
        print("from method demo of class A")

    def abc(self):
        print("from method abc of class A")

x = A()

class B:
    role = 'admin'
    emd_id = 5

    def xyz(self):
        print("from method xyz of class B")

y = B()
# print(y.role, y.emd_id)
# print(y.xyz())
# print(y.name, y.age, y.id)
# print(y.demo())
# print(y.abc())
print(y.grade)
print(y.abc())

# print(x.name, x.age, x.id)
# print(x.demo())
# print(x.abc())

"""
types of inheritance:
1. single level inheritance
2. multilevel inheritance
3. multiple inheritance
"""

class C(A,B):
    grade = 3
    
    def cclass(self):
        print("from method cclass of class C")

abc = C()
# print(abc.role, abc.emd_id)
# print(abc.xyz())
# print(abc.grade)
# print(abc.cclass())   
# abc.cclass()
# print(abc.name, abc.age, abc.id)
# print(abc.demo())
# print(abc.abc())