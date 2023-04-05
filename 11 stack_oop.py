class Stack:
    def __init__(self):
        self.__stack_list = [] #__makes it private and will be accessed only within a fn


    def push(self, val):
        self.__stack_list.append(val)


    def pop(self):
        val = self.__stack_list[-1]
        del self.__stack_list[-1]
        return val

    def print_stack(self): #return stuck
        return self.__stack_list


stack_object = Stack()

stack_object.push(3)
stack_object.push(2)
stack_object.push(1)

print(stack_object.print_stack())
print(stack_object.pop())
print(stack_object.pop())
print(stack_object.pop())

print(stack_object.print_stack())


# sub class in heriting Stack
class AddingStack(Stack):
    def __init__(self): # initializing the class
        Stack.__init__(self) #initializing the inherited class
        self.__sum = 0 #defining a private value, sum

    def get_sum(self):  #returns the sum
        return self.__sum

    def push(self, val): #push a value to the private stack inherited from parent
        self.__sum += val  #for very value passed add it to sum
        Stack.push(self, val) #push it to stack

    def pop(self):
        val = Stack.pop(self) #remove from stack
        self.__sum -= val   #reduce sum 
        return val


stack_object = AddingStack() #

for i in range(5):
    stack_object.push(i)
print(stack_object.get_sum())

for i in range(5):
    print(stack_object.pop())
    