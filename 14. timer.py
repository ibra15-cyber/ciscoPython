def two_digits(val):
    s = str(val)
    if len(s) == 1:
        s = '0' + s #if len of converted digit is 1 append 0 infront and return it
    return s


class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0): #constructor initializina class instances
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self): #string fn, default just like __init__ and passing our instance variables and concatenating them aka making them strings
        return two_digits(self.__hours) + ":" + \
               two_digits(self.__minutes) + ":" + \
               two_digits(self.__seconds)

    def next_second(self): 
        self.__seconds += 1 #keep adding one to seconds, when it 60, make second 0 and increment min when min is 60 make min 0 and incre hr etc
        if self.__seconds > 59:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes > 59:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours > 23:
                    self.__hours = 0

    def prev_second(self): #handles decreament of s, m and hr 
        self.__seconds -= 1
        if self.__seconds < 0:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes < 0:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours < 0:
                    self.__hours = 23


timer = Timer(23, 59, 59)
print(timer) #the string fn
timer.next_second() #start increment fn
print(timer) 
timer.prev_second()
print(timer)
    