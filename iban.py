# IBAN Validator.

iban = input("Enter IBAN, please: ")
iban = iban.replace(' ','') #Remove any whitespace

if not iban.isalnum(): #if not alphanumeric
    print("You have entered invalid characters.")
elif len(iban) < 15: #lenght can be lsess 15 and more than 31
    print("IBAN entered is too short.")
elif len(iban) > 31:
    print("IBAN entered is too long.")
else:
    iban = (iban[4:] + iban[0:4]).upper() #get the fourth char to the end, concatenate it with the first 4 and make it upper
    print(iban)
    iban2 = ''
    for ch in iban:
        if ch.isdigit(): #if a character in the iban string is a digit, conc it to iban2
            iban2 += ch
        else:
            iban2 += str(10 + ord(ch) - ord('A')) #else add 10 to the ord value and sub ord('A'). whatever you get make it str
    iban = int(iban2) #turn it back to int and assign to iba 
    print(iban)
    if iban % 97 == 1: #if it is not divi by 97 it is valid else invalid
        print("IBAN entered is valid.")
    else:
        print("IBAN entered is invalid.")
    