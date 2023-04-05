# import pygame

# run = True
# width = 400
# height = 100
# pygame.init()
# screen = pygame.display.set_mode((width, height))
# font = pygame.font.SysFont(None, 48)
# text = font.render("Welcome to pygame", True, (255, 255, 255))
# screen.blit(text, ((width - text.get_width()) // 2, (height - text.get_height()) // 2))
# pygame.display.flip()
# while run:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT\
#         or event.type == pygame.MOUSEBUTTONUP\
#         or event.type == pygame.KEYUP:
#             run = False


# import math
# result = math.e != math.pow(2,4)

# print(result)

# print(math.pow(2,4))

# print(ord("A"))

# print(chr(65))

# string = "my name is "

# stringModi = string[0:-3]
# print(stringModi)

# string = "am"
# string = "n" + string
# string = string + "e"
# print(string)
# print(len("""
# """))

# string = "[" + "alpha".center(10,"*") + "]"
# print(len(string))
# print(string)

# print("www.cisco.com".lstrip("w"))

# a = "string"
# print(a.split(","))

# string  = 'how are you doing'
# print(sorted(string))
# print(string.split())

# lisst = ["a", "c", "b"]
# print(sorted(lisst))

# try:
#     print("1")
#     x = 1 / 0
#     print("2")
# except:
#     print("Oh dear, something went wrong...")

# print("3")
    


# class A:
#     A = 1


# print(hasattr(A,'A'))

# class A:
#     def a(self):
#         print('a')


# class B:
#     def a(self):
#         print('b')


# class C(B,A):
#     def c(self):
#         self.a()


# o = C()
# o.c()


# from random import seed, randint

# seed()

# data = [randint(-10, 10) for x in range(5)] #give me 5 random variables from -10 to 10
# print(data)

# filtered = filter(lambda x: x >= 0 and x%2 == 0, data) #filter my list, create another list and only return values in list > 0 and even
# print(filtered)

# import os, sys
# print(os.name()) #uname
# print(os.environ) #
# print("**********************************************")
# print(sys.path)
# os.mkdir("my_directory")
# os.rmdir("my_directory")
# print(os.listdir())
# os.chdir("packages") #cd
# print(os.getcwd()) 


# from datetime import date

# today = date.today()

# print("Today:", today)
# print("Year:", today.year)
# print("Month:", today.month)
# print("Day:", today.day)
    

# from datetime import date

# my_date = date(2019, 11, 4)
# print(my_date) #2019-11-04


# from datetime import date
# import time

# timestamp = time.time() #time from january 1 1970
# print("Timestamp:", timestamp)

# d = date.fromtimestamp(timestamp) #formating a time.time obj in a date format
# print("Date:", d)
     
# isof = date.isoformat(d)
# print("Iso: ", isof)

# dob = date.fromisocalendar(1990, 2, 2)
# print(dob)
# print(date.month)



# from datetime import date

# d = date(1991, 2, 5)
# print(d)

# d = d.replace(year=1992, month=1, day=16)
# print(d)

# #day of the week
# from datetime import date

# d = date(2019, 11, 4)
# print(d.weekday())

# from datetime import date

# d = date(2019, 11, 4)
# print(d.isoweekday())


# import time

# class Student:
#     def take_nap(self, seconds):
#         print("I'm very tired. I have to take a nap. See you later.")
#         time.sleep(seconds)
#         print("I slept well! I feel great!")

# student = Student()
# student.take_nap(5)
    

# import time

# timestamp = 1572879180
# print(time.ctime(timestamp))

# import time

# timestamp = 1572879180
# print(time.gmtime(timestamp))
# print(time.localtime(timestamp))
    
# from datetime import date

# d = date(2020, 1, 4)
# print(d.strftime('%Y/%m/%d'))
    
    
import calendar

# print(calendar.calendar(2020))

# calendar.prcal(2020)

#for specific month
# print(calendar.month(2020, 11))

# calendar.firstweekday(calendar.SUNDAY) #change first day of the week to sunday

x = "\\"
print(len(x))