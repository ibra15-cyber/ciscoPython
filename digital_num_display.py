digits = [ '1111110',  	# 0
	   '0110000',	# 1
	   '1101101',	# 2
	   '1111001',	# 3
	   '0110011',	# 4
	   '1011011',	# 5
	   '1011111',	# 6
	   '1110000',	# 7
	   '1111111',	# 8
	   '1111011',	# 9
	   ]



def print_number(num): #will pass a num when i need you. hardcodded or manual
	global digits      #accessible everywhere in the code 
	digs = str(num)    # make a string of number i will be passing
	lines = [ '' for lin in range(5) ] #['', '', '', '', '']
	for d in digs:	#iterating the string, ie my enter digit say 105 for each of them
		segs = [ [' ',' ',' '] for lin in range(5) ] #make 5 of this list [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
		ptrn = digits[ord(d) - ord('0')]	#find the diff of each numb ch in ord and subtra that of 0
		if ptrn[0] == '1':					#if the first convert == 1
			segs[0][0] = segs[0][1] = segs[0][2] = '#' # [['#', ' ', '#'], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

		if ptrn[1] == '1':
			segs[0][2] = segs[1][2] = segs[2][2] = '#'
		if ptrn[2] == '1':
			segs[2][2] = segs[3][2] = segs[4][2] = '#'
		if ptrn[3] == '1':
			segs[4][0] = segs[4][1] = segs[4][2] = '#'
		if ptrn[4] == '1':
			segs[2][0] = segs[3][0] = segs[4][0] = '#'
		if ptrn[5] == '1':
			segs[0][0] = segs[1][0] = segs[2][0] = '#'
		if ptrn[6] == '1':
			segs[2][0] = segs[2][1] = segs[2][2] = '#'
		for lin in range(5):
			lines[lin] += ''.join(segs[lin]) + ' '
	for lin in lines:
		print(lin)


# print_number(int(input("Enter the number you wish to display: ")))

number = int(input("Enter the number you wish to display: "))

print_number(number)

# print([[' ',' ',' '] for lin in range(5)])
