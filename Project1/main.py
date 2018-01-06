'''
__author__	: Priyank Parmar
__tested_on__	: 
__description__ ; Project has following functionalities
		  1. Takes input from the user (Website name, Email ID, Username, Password)
		  2. Encrypt all the input
		  3. Set all them in a single string
		  4. Write the encrypted string into file
'''
def websiteParse(str):
	''' Function to parse Website name from full name
	for eg --> Input  : 'www.facebook.com' 
		   Output : 'facebook'
	
 	Input arguments: String to be parsed
	
	Output	: Parsed string '''
	str = str.split('.')
	return str[1]

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

def encryption(str):
	''' Encryption :
	    combination of (Base-64 --> Hex --> rot13)
	
	Input arguments :
	str : String to be encrypted

	Output:
 	Encrypted string '''
	return 	str.encode('base-64','strict').encode('hex','strict').encode('rot13','strict')

def decryption(str):
	''' Decryption :
	    combination of (rot13 --> Hex --> Base-64)
	
	Input arguments :
	str : String to be decrypted

	Output:
 	Decrypted string '''
	return  str.decode('rot13','strict').decode('hex','strict').decode('base-64','strict')

def strSetIn200(str):
	''' Function to set the string into fixed sized string (of 200)
	
	Input arguments:
	str	: String to be set
	
	Output  : Fixed sized string of 10 '''
	# Declaration of string
	mainStr = ['.']*200 
	mainStr = "".join(mainStr)	# Converting list into string
	return mainStr[len(str):] + str[:len(str)]

def strParseFrom200(str):
	''' Function to parse string from fixed sized string(of 200)
	
	Input arguments:
	str	: String to parse
	
	Output	: Parsed String '''
	str = str.split('.')
	return str[len(str)-1]

def lineReplace( lineNumber, str):
	'''Function to replace a line in file
	
	Input arguments:
	lineNumber : Number of line to be replaced(int)
	str	   : String to write into file
	
	Output:
	None '''
	# Reading file content in variable
	try:
		file = open( 'data.txt', 'r')
		data = file.readlines()
		file.seek(0)
	
		# Altering content 	
		data[lineNumber-1] = str +'\n'
	
	# Writing into file
	file = open( 'data.txt', 'w+')
	file.writelines(data)
	file.close()
	return 

def invalidPasswordDisplay():
 	print "====================================="
	print "NOTE :"
	print "Password Should contain at least :"
	print "One Upper,One Lower Case Letter"
	print "One numeric and special character"
	print "TRY AGAIN"
	print "====================================="
	return 

def invalidWebsiteNameDisplay():
	print "====================================="
	print "NOTE :"
	print "Enter Website Name in following format"
	print "Eg : www.websitename.com"
	print "====================================="
	return 

def main():
	## Take input from user
	while True:
		websiteName = raw_input('Enter Website Name :')
		if websiteName[0:4] == 'www.' or websiteName[0:4] == 'WWW.':
			break
		else:
			invalidWebsiteNameDisplay()
	emailId = raw_input('Enter email-id :')
	userName = raw_input('Enter username :')
	while True:
		password = raw_input('Enter Password :')
		if isPasswordConstrained(password) == 'Valid':
			break
		else:
			invalidPasswordDisplay()

	## website name after parsing
	website = websiteParse(websiteName)	 
	print website

	## Encrytion  and set them of all 
	encry200Website  = strSetIn200(encryption(website))
	encry200emailId  = strSetIn200(encryption(emailId))
	encry200userName = strSetIn200(encryption(userName))
	encry200password = strSetIn200(encryption(password))
	
	## Set all them in a single string
	encryStringLine = encry200Website  + encry200emailId + \
		          encry200userName + encry200password
	print "Encrypted Line :", encryStringLine
	
	## Write encrypted string into file
	lineReplace( 1, encryStringLine)

	## Parse Encrypted String Line
	encry200WebsiteParse = encryStringLine[0:200]
	encry200emailIdParse = encryStringLine[200:400]
	encry200userNameParse = encryStringLine[400:600]
	encry200passwordParse = encryStringLine[600:800]	
	
	parsedWebsite = strParseFrom200(encry200WebsiteParse)
	parsedEmailId = strParseFrom200(encry200emailIdParse)
	parsedUsername = strParseFrom200(encry200userNameParse)
	parsedPassword = strParseFrom200(encry200passwordParse)
	
	decryptedWebsite = decryption(parsedWebsite)
	decryptedEmailId = decryption(parsedEmailId)
	decryptedUsername = decryption(parsedUsername)
	decryptedPassword = decryption(parsedPassword)
	
	print "Decrypted Website :", decryptedWebsite
	print "Decrypted Email ID :", decryptedEmailId
	print "Decrypted Username :", decryptedUsername
	print "Decrypted Password :", decryptedPassword
	return

if __name__ == '__main__':
	main()
