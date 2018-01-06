'''
__author__ 	: Priyank Parmar
__tested_on__	: 4th June, 2017
__description__ : To test the constrains of password string
'''
# Taking input from user
password_str = raw_input('Enter Password :')
# Printing Password to output screen
print "Entered Password is :", password_str
print "============================================="
# Iterating to string
print "Iterating in String"
for i in password_str:
	print i
print "============================================="
# To check whether string constains white space
'''
if (' ' in password_str) == True:
	print "Password contain White Space"
else:
	print "Password does not contain White Space"
'''
if any(x.isspace() for x in password_str) == True:
	print "Password contain White Space"
else:
	print "Password does not contain White Space"
print "============================================="
# To check whether string is long enough or not
if (len(password_str) >= 8) == True:
	print "Password is at least 8 character long"
else:
	print "Password is shorter than 8 character"
print "============================================="
# To check whether string contains at least one Upper Case
if any(x.isupper() for x in password_str) == True:
	print "Password contains at least one Upper Case"
else:
	print "Password does not contain Upper Case"
print "=============================================" 
# To check whether string contains at least one Lower Case
if any(x.islower() for x in password_str) == True:
	print "Password contains at least one Lower Case"
else:
	print "Password does not contain Lower Case"
print "============================================="
# To check whether string contains at least one digit
if any(x.isdigit() for x in password_str) == True:
	print "Password contain one digit"
else:
	print "Password does not contain any digit"
print "============================================="
# To check whether string contains any special character
special_char = "~!@#$%^&*()_+"
for i in password_str:
	if i in special_char:
		print "Password contain special character"
		break
print "============================================="	
