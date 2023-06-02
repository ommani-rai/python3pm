class Animal:
    name = 'animal'

    def eat(self):
        # print("from eat method of class Animal")
        return self.name

    def run(self):
        print("from run method of class Animal")

class dog(Animal):
    def bark(self):
        print("from bark method of class dog")

obj1 = dog()
# print(obj1.eat())
# print(obj1.run())
# print(obj1.bark())

class bird(Animal):
    def fly(self):
        print("from fly method of class bird")
obj2 = bird()
print(obj2.name)
asdf = obj2.eat()
print(asdf)
print(obj2.run())
print(obj2.fly())
