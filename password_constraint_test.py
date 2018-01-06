'''
__author__ 	: Priyank Parmar
__tested_on__	: 4th June, 2017
__description__ : Implementation of function test the constraints of password string and Validity
'''
def isPasswordConstrained(password_str):
	''' Test Validity of Input Password
	    Password Constraints :
	    Rule 1: It should not contain any white spaces
	    Rule 2: It should contain at least one uppercase letter
	    Rule 3: It should contain at least one lowercase letter
	    Rule 4: It should contain at least one numeric 
	    Rule 5: It should contain at least one special character
		
	    Input arguments:
	    password_str -- Password string to test
	
	    Output:
	    Valid or Invalid '''
	# Special Character Test
	hasSpecialChar = False
	special_char = "~!@#$%^&*()_+"
	for i in password_str:
		if i in special_char:
			hasSpecialChar = True
			break
	# All Password Constraint Test
	if (any(x.isspace() for x in password_str) == False) and \
	   any(x.isupper() for x in password_str) and \
	   any(x.islower() for x in password_str) and \
	   any(x.isdigit() for x in password_str) and \
	   hasSpecialChar and len(password_str) >= 8 :	   
		return "Valid"
	else:
		return "Invalid"


# Taking input from user
password_str = raw_input('Enter Password :')
# Printing Password to output screen
print "Entered Password is :", isPasswordConstrained(password_str)

