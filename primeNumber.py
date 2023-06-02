# using for loop
num = int(input("enter a number"))

if num == 1:
    print("1 is not a prime number")
elif num > 1:
    for i in range(2,num):
        if (num % i == 0):
            print(f"{num} is not a prime number")
            break
    else:
        print(f"{num} is a prime number")