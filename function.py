def welcome(para, para1, para2):
    print("welcome to python class")
welcome('arg1', 'arg2', 'arg3')

# arguments
"""
types of arguments:
1. required arguments
2. default arguments
3. keyword arguments
4. variable length arguments
"""

# 1. reuqired arguments
def my_function(fruit):
    print(f"the fruit name is: {fruit}")
my_function("apple")

# 2.default arguments
def sum(a = 1, b=2):
    print(f"the sum of  {a} and {b} is: {a+b}")

sum(a =3, b = 6)

# 3. keyword arguments
def divide(c, d):
    print(f"the division of {c} and {d} is: {c/d}")
divide(d=5,c=10)

# 4. variable length arguments
def sumofno(*num):
    print(num[3])

sumofno(2,3,4,"abc", True)



def items(food):
    for key, value in food.items():
        print(f"{key} : {value}")
    # for item in food:
    #     print(item)

# lists = ['apple', "banana", "kiwi"]
tuples = ('apple', "banana", "kiwi")
dic = {
    1: "apple",
    2: "banana",
    3: "kiwi"
}
# passing list in function
# items(lists)
# passing tuples in function
# items(tuples)
# passing dictionary in function
items(dic)


# Return in Function
def sum_of_number(a, b, c):
    # d = a + b + c
    # return d
    return a+b+c

# print(sum_of_number(2,3,4))
sum = sum_of_number(2,3,4)
print(sum)