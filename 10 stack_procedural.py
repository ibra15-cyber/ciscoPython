stack = []


def push(val):
    stack.append(val)


def pop():
    val = stack[-1]
    print(val)
    del stack[-1]
    return val


push(3)
push(2)
push(1)
print(stack)

print(pop())
print(pop())
# print(pop())

print(stack)
    