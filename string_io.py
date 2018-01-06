'''
__author__ 	: Priyank Parmar
__tested_on__	: 4th June, 2017
__description__	: To implement String input output and Various operations 
'''

## Simple input and output string
# Taking input string
str = raw_input('Enter String :')
# Diplay input string
print "Entered String is :" + str


## Taking string input and parsing it
# Taking input string
str1 = raw_input('Enter String(8 Letter Long) to parse :')
# Printing specific indexed letter
print "str1[0] :", str1[0]
print "str1[5] :", str1[5]  
print "str1[1:3] :", str1[1:3]


## Parsing string content for eg "upwork" from "www.upwork.com"
# Taking input from user
str2 = raw_input("Enter Website Name :")
# String parsing
print "Entered Website is :", str2[4:len(str2)-4]


## String comparison if else testing
# Taking input from user
str3 = raw_input("Enter String to be Matached with 'Priyank':")
# Matching Strings
if str3 == "Priyank":
	print "String Matching"
else:
	print "String Not Matching"

