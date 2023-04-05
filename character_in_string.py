word = input("Enter the word you wish to find: ").upper() #take a input and make it upper
strn = input("Enter the string you wish to search through: ").upper() #take a string that will be searched to find our input above

found = True
start = 0

for ch in word: 	#search characters in input
	pos = strn.find(ch, start) #find that character in our string from index 0
	if pos < 0:			#if we fail to find 
		found = False	#found is false break 
		break
	start = pos + 1   #if ch is found, increment start position
if found:
	print("Yes") #found print yes
else:
	print("No")
	   