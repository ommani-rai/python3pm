# class self:
#     # def __init__(self, name, age, gender):

#     def display(self, name, age, gender):
#         self.name1 = name
#         self.age1 = age
#         self.gender1 = gender
#         print("name: ", self.name1)
#         print("age: ", self.age1)
#         print("gender: ", self.gender1)

# obj = self()
# # obj.name1 = "shyam"
# # obj.age1 = 23
# # obj.gender1 = "female"


# obj.display('rhaul', 2323, 'male')
# obj.name1 = 'asdfasdf'
# print(obj.name1)


# # class Employee:
# #     no_of_leaves = 0

# #     def __init__(self, your_name,your_salary, your_role ):
# #         self.name = your_name
# #         # emp.name
# #         self.salary = your_salary
# #         self.role = your_role

    
# #     def printdetails(self):
# #         return f"Name is {self.name} . salary is {self.salary} and role is {self.role}"
    
# # emp = Employee()
# # # emp = Employee('parashmani', 1222, 'admin')
# # # print(emp.name)
# # # print(emp.salary)
# # # print(emp.role)

# # emp.name = "parashmani"
# # emp.salary = 1222
# # emp.role = 'admin'
# # # print(emp.name)
# # # print(emp.salary)
# # # print(emp.role)

# # print(emp.printdetails()) 

class self:
    def display(self):
        print("name: ", self.name)
        print("age: ", self.age)
        print("gender: ", self.gender)

    def info(self):
        print("from info method")
        self.display()

a = self()
a.name = "rahul"
a.age = 23
a.gender = "male"

a.info()
