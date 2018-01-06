'''
__author__ 	: Priyank Parmar
__tested_on__	: 4th June, 2014
__description__ : Function for encryption and decryption of string
'''
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

## Input from the user
str = raw_input('Enter String :')
encrypted_str = encryption(str)
print "Encrypted String : ", encrypted_str
print "Length of Encrypted String :", len(encrypted_str)
print "Decrypted String : ", decryption(encrypted_str)

