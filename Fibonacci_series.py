# 0 1 1 2 3 5 8 13 21

# n1 = 0
# n2 = 1
# n3 = n1 + n2 
# fibonacci series using for loop
a = 0
b = 1
num = int(input("enter a number"))

if num == 0:
    print(a)
elif num == 1:
    print(a)
    print(b)
# print(a)
# print(b)
if num >1:
    print(a, end=" ")
    print(b, end=" ")
    for i in range(2, num): 
        c = a + b
        a = b
        b = c
        print(c, end=" ")


"""
# fibonacci series using Recursion
def fibonaci(num): 
    # 4
    if num <= 1:
        return num
    else:
        return  (fibonaci(num -1) + fibonaci(num -2))
    # fib(3) + fib(2)

num = int(input("enter a number"))
for i in range(num):
    print(fibonaci(i))

"""
