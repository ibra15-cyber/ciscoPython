import math


class Point:
    def __init__(self, x=0.0, y=0.0): #init our constructor with 0 for both x and y
        self.__x = x #pass them to our obj instances
        self.__y = y

    def getx(self): #
        return self.__x #returns x 

    def gety(self):
        return self.__y #return y

    def distance_from_xy(self, x, y):
        value = math.hypot(abs(self.__x - x), abs(self.__y - y)) #finds distance
        print("xy: ", value)
        return value

    def distance_from_point(self, point): #find distance point from x and y
        return self.distance_from_xy(point.getx(), point.gety())


point1 = Point(0, 0) 
point2 = Point(1, 1) #goes in first and gets the distance_from xy


print(point1.distance_from_point(point2))

print(point2.distance_from_xy(2, 0))
    