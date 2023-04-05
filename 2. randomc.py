# # c0 = int(input("Enter a number: "))

# # while c0 >= 0:
# #     if c0 % 2 == 0:
# #         print(c0/2)
# #     else:
# #         if c0 == 1:
# #             continue
# #         print((3*c0) + 1 )



# for i in range(1, 11):
#     if i%2 == 0:
#         continue
#     print(i)

# i = 0
# while i<10:
#     i = i+ 1
#     if i%2 == 0:
#         continue
#     print(i)

# for i in "john@gmail.com":
#     if i == "@":
#         break
#     print(i, end="")

# print()
# for i in "0165031806510":
#     if i == "0":
#         i = "x"
#     print(i, end="")

# for i in range(1):
#     print("#")
# else:
#     print("#")

# var = 0
# while var < 6:
#     var += 1
#     if var % 2 == 0:
#         continue
#     print("#")


# var = 1
# while var < 10:
#     print("#")
#     var = var << 1


# vals = [0, 1, 2]
# vals.insert(0, 1)
# print(vals)
# del vals[1]
# print(vals)

# alist = [1,2,3]
# alist.insert(0, 0)
# print(alist)

# my_list = [1, 2, 3]
# for v in range(len(my_list)):
#     my_list.insert(1, my_list[v])
# print(my_list)



# tuple_1 = (1, 2, 4, 8)
# tuple_2 = 1., .5, .25, .125

# print(tuple_1)
# print(tuple_2)

# value = int(input('Enter a natural number: '))
# print('The reciprocal of', value, 'is', 1/value)

# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     # Insert your code here.
#     print(k[0])

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2)) + 1)


my_list =  ['Mary', 'had', 'a', 'little', 'lamb']

# def my_list(my_list):
#     del my_list[3]
#     my_list[3] = 'ram'

# del my_list[3]
# my_list[3] = 'ram'

# print(my_list)


# dictionary = {'one': 'two', 'three': 'one', 'two': 'three'}
# v = dictionary['one']

# for k in range(len(dictionary)):
#     v = dictionary[v]

# print(v)




# import math
# print(math.sin(math.pi/2))

# from platform import platform

# # print(platform())
# # print(platform(1))

# print(platform(0, 1))


# from platform import machine

# print(machine())


# from platform import processor

# print(processor())


# from platform import system

# print(system())

# from platform import version

# print(version())


# from platform import python_implementation, python_version_tuple

# print(python_implementation())

# for atr in python_version_tuple():
#     print(atr, end='')

# import random
# print(dir(random))

import sys

for p in sys.path:
    print(p)





