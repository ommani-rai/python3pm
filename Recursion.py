# factorial of a number using for loop
"""
factorial(6) = 6 * factorial(5) => 6 * 5 *4 *3 *2 *1
factorial(5) = 5 *factorial(4)
factorial(n) = n *factorial(n-1)
6 = 6 * 5 * 4 * 3 * 2 * 1
5 = 5 * 4 * 3 * 2 * 1
4 = 4 * 3 * 2 * 1
3 = 3 * 2 * 1
2 = 2 * 1
1 = 1
0 = 1

"""
num = int(input("enter a number"))
if num < 0:
    print("invalid input")
elif num ==0:
    print(1)
elif num == 1:
    print(1)
else:
    fact = 1
    for i in range(2, num + 1): # 2, 3 , 4
        fact = fact * i
        # fact = 1 * 2
        # fact = 2 * 3 = 6
        # fact = 6 *4 = 24
    print(fact)



"""
def factorial(n):
    if n < 0:
        return 0
    elif n ==0:
        return 1
    elif n == 1:
        return 1
    else:
        return (n*factorial(n-1))
                # 4 * factorial(3)
                # 4 * 3 * factorail(2)
                #  4 * 3 * 2 * factorial(1)
                #  4 * 3 * 2 * 1 = 24
    
num = int(input('enter a number'))
x = factorial(num)
print(x)

"""