"""
exception handling -> handling logic error in the program

try:
    a = int(input("enter the value of a: "))
    b = int(input("enter the value of b: "))
    sum = a + b
    division = a / b
    # print(sum)
    print(division)
# except Exception as e:
except ZeroDivisionError as e:
    # print("enter the valid number only")
    print(e)
    # print("do not pass the value of b as 0")
"""
try:
    a = int(input("enter the value of a: "))
    b = int(input("enter the value of b: "))
    sum = a + b 
    division = a / b 
    # print(sum) 
    print(division) 
except:
    print("division by zero error")

print("end of the program")



IndexError
ValueError
