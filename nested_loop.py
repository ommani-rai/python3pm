# for i in range(4): # 0 1 2 3
#     for j in range(4): # 0 1 2 3
#         print(i)
#         print(j)
    # print(i)

    # output 0 0 0 1 0 2 0 3 1 0 1 1 1 2 1 3 2 0 2 1 2 2 2 3 3 0 3 1 3 2 3 3

"""
****
****
****
****
"""

# for i in range(4): # 0 1
#     for j in range(4): #0 1 2 3
#         print("*", end="") # * * * *
#     print("")


"""
*
**
***
****
*****
"""
# for i in range(5): # 0 1 2
#     for j in range(i+1): # 0, 0 1, 0 1 2
#         print("*", end="")
#     print("")


"""
*****
****
***
**
*
"""
# for i in range(5): # 0 1 2 
#     for j in range(5-i):
#         print('*', end="")
#     print("")

"""
5
5 4
5 4 3
5 4 3 2
5 4 3 2 1 
"""
# for i in range(5, 0, -1): # 0 4
#     for j in range(5, i-1, -1): # 5 5 4
#         print(j, end="")
#     print("")


"""
5 4 3 2 1
4 3 2 1
3 2 1
2 1
1
"""
for i in range(5, 0, -1): # 5
    for j in range(i, 0, -1):
        print(j, end="")
    print("")


"""
5 4 3 2 1
5 4 3 2
5 4 3
5 4 
5
"""