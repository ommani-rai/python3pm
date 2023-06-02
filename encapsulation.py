class info:
    name = "ommani"
    __name = "ram"
    __age = 23
    __role = "admin"
    def __init__(self):
        print("from init method")
        self.__area()


    def __area(self):
        print("from private method area")
    
    def displayInfo(self):
        print("this method will return some info", self.__name, self.__age, self.__role)

obj = info()
# obj.__area()
print(obj.name)
# print(obj.__name)
obj.displayInfo()