'''
__author__ 	: Priyank Parmar
__tested_on__	: 4th June, 2017
__description__ : To test different encoding and decoding methods
'''
## Taking the Input from user
str = raw_input('Enter String :')
print "=================================================="
## Encoded String
print "Encoded Strings"
# UTF-8 Encoding
encoded_str_utf_8 = str.encode('UTF-8','strict')
print "Encoded String [UTF-8] :", encoded_str_utf_8

# UTF-16 Encoding
encoded_str_utf_16 = str.encode('UTF-16','strict')
print "Encoded String [UTF-16] :", encoded_str_utf_16

# base-64 Encoding
encoded_str_base_64 =  str.encode('base-64','strict')
print "Encoded String [Base-64] :", encoded_str_base_64

# hex Encoding
encoded_str_hex =  str.encode('hex','strict')
print "Encoded String [Hex] :", encoded_str_hex

# rot13 Encoding
encoded_str_rot_13 = str.encode('rot13','strict')
print "Encoded String [rot13] :", encoded_str_rot_13
print "=================================================="

## Decoded String
print "Decoded Strings"
# UTF-8 Decoding
print "Decoded String [UTF-8] :", encoded_str_utf_8.decode('UTF-8','strict')

# UTF-16 Decoding
print "Decoded String [UTF-16] :", encoded_str_utf_16.decode('UTF-16','strict')

# base-64 Decoding
print "Decoded String [Base-64] :", encoded_str_base_64.decode('base-64','strict')

# hex Decoding
print "Decoded String [Hex] :", encoded_str_hex.decode('hex','strict')

# rot13 Decoding
print "Decoded String [rot13] :", encoded_str_rot_13.decode('rot13','strict')
print "=================================================="

## Encryption combination of (Base-64 --> Hex --> rot13
print "Encryption"
encrypted_str = str.encode('base-64','strict').encode('hex','strict').encode('rot13','strict')
print encrypted_str

## Decryption combination of (rot13 --> Hex --> Base-64)
print "Decryption"
decrypted_str = encrypted_str.decode('rot13','strict').decode('hex','strict').decode('base-64','strict')
print decrypted_str

