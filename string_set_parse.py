'''
__author__	: Priyank Parmar
__tested_on__	: 
__description__ : To set the string into fixed length and parse it
'''
def strSetIn10(str):
	''' Function to set the string into fixed sized string (of 10)
	
	Input arguments:
	str	: String to be set
	
	Output  : Fixed sized string of 10 '''
	# Declaration of string
	mainStr = ['.']*10 
	mainStr = "".join(mainStr)	# Converting list into string

	return mainStr[len(str):] + str[:len(str)]

def strParseFrom10(str):
	''' Function to parse string from fixed sized string(of 10)
	
	Input arguments:
	str	: String to parse
	
	Output	: Parsed String '''
	str = str.split('.')
	return str[len(str)-1]

def main():
	# User input
	str = raw_input('Enter String of length less than 9 :')
	print "String after Setting :", strSetIn10(str)

	print "String afetr Parsing :", strParseFrom10(strSetIn10(str))
	return

if __name__ == '__main__':
	main()

