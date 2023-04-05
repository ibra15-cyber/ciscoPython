file = open("./text.txt", "r")
# print(file.read()) #reads everything
# print(file.readline()) #reads the whole line
# print(file.readline(1)) #reads the first char
# print(file.readlines()) #reads the lines on one line and separated by /n
# print(file.readlines(1)) #reads the lines only the first line



# # iterating without a method 
# from os import strerror

# try:
# 	ccnt = lcnt = 0
# 	for line in open('text.txt', 'rt'):
# 		lcnt += 1
# 		for ch in line:
# 			print(ch, end='')
# 			ccnt += 1
# 	print("\n\nCharacters in file:", ccnt)
# 	print("Lines in file:     ", lcnt)
# except IOError as e:
# 	print("I/O error occurred: ", strerror(e.errno))

from os import strerror

data = bytearray(10)

for i in range(len(data)):
    data[i] = 10 + i

try:
    bf = open('file.bin', 'wb')
    bf.write(data)
    bf.close()

    file =  open('file.bin', "rb")
    for i in file:
        print(i, end="")
except IOError as e:
    print("I/O error occurred:", strerror(e.errno))

# Your code that reads bytes from the stream should go here.
    
    