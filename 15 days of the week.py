class WeekDayError(Exception):
    pass


class Weeker:
    __names = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

    def __init__(self, day):
        try:
            self.__current = Weeker.__names.index(day) #create an instant private variable and assing the name of the index that correspond days you chose
        except ValueError: #any input other than expect , flag exception
            raise WeekDayError

    def __str__(self):
        return Weeker.__names[self.__current] #string printing 

    def add_days(self, n):  ###add a days takes the number of days to add, but since we got only 7 days we also take the reminder in module 7
        self.__current = (self.__current + n) % 7

    def subtract_days(self, n): #same with subtra
        self.__current = (self.__current - n) % 7


try:
    weekday = Weeker('Mon') #we make an obj weekday and initiz our constr with "mon"
    print(weekday) #this will print mon
    weekday.add_days(15) #add 15 to mon will add 15 to 0 i.e index of 'mon' == 15%7 1 ie tues
    print(weekday) # i expect tues
    weekday.subtract_days(23) #sub 23 1-23 = -22%7 = 6 whihc is sun
    print(weekday)

    weekday = Weeker('Monday') #this will raise error bc not in our list
except WeekDayError:
    print("Sorry, I can't serve your request.")
    