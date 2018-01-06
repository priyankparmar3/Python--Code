'''
__author__	: Priyank Parmar
__tested_on__	: 
__description__ : Function to implement read and write a specific line from txt file
'''

import linecache

def readLine( fileName, lineNumber):
	''' Function to implement reading of specific line from file
	
	Input arguments:
	fileName   : Name of text file
	lineNumber : Number of line (int)

	Output : Read string '''
	linecache.clearcache()
	return linecache.getline( fileName, lineNumber)

def writeLine( fileName, lineNumber, str):
	''' Function to implement writing a string to specific line line
	
	Input arguments:
	fileName   : Name of text file
	lineNumber : Number of line (int)
	str	   : String to write '''
	

def main():
	# User input
	line =  raw_input('Enter line number to read :')
	# print the line
	print "Data is : ", readLine('data.txt',int(line))
	# Writing specific line
	# writeLine('data.txt',2,"Hello")
	

if __name__ == '__main__':
	main()
