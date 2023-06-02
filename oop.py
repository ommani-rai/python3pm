"""
oop => object oriented programming
main pillars of oop
1. class
2. object
3. polymorphism
4. inheritance
5. encapsulation
6. data abstraction


1. class
animal => elephant, dog => eat(), run()
"""
"""
color_outside = "red"
class Animal:
    color = "yellow"
    def eat(self, food):
        print(f"within the method", food, self.color)

    def run(self):
        print('run method within the class') 

print(color_outside)

dog = Animal()
x = Animal()
c = Animal()
print(x.color)
print(dog.color)
a = dog.eat("apple")
b = dog.run()


color_red - snake case naming convention
colorRed - camel case naming convention
ColorRed - pascal case naming convention
color-red - kebab case naming convention

"""

class Employee():
    def emp_detail(self, name, id, role):
        print(f"the name of the employee is: {name}")
        print(f"the emp_id of the employee is: {id}")
        print(f"the role of the employee is: {role}")

emp1 = Employee()
emp1.emp_detail("ram", 1, "superviser")

emp2 = Employee()
emp2.emp_detail("shyam", 2, 'CEO')

emp3 = Employee()
emp3.emp_detail("abc", 3, "xyz")

# list1 = [name:"ram", id= 1, role="ceo"]
# list2 = [name:"ram", id= 1, role="ceo"]
# list3 = [name:"ram", id= 1, role="ceo"]
# list4 = [name:"ram", id= 1, role="ceo"]
# list5 = [name:"ram", id= 1, role="ceo"]