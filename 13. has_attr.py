class ExampleClass:
    a = 1
    def __init__(self):
        self.b = 2


example_object = ExampleClass()

print(hasattr(example_object, 'b')) #after initializing it can see it
print(hasattr(example_object, 'a'))
print(hasattr(ExampleClass, 'b')) #but before initializing it doenst know about b
print(hasattr(ExampleClass, 'a'))



class Sample:
    gamma = 0 # Class variable.
    def __init__(self):

        self.alpha = 1 # Instance variable.
        self.__delta = 3 # Private instance variable.


obj = Sample()
obj.beta = 2  # Another instance variable (existing only inside the "obj" instance.)
print(obj.__dict__)
print(Sample.__dict__)

print(hasattr(obj, "gamma"))  #does obj has an attri 'gamma' it says true
print(hasattr(Sample, "gamma"))



