'''
__author__	: Priyank Parmar
__tested_on__	: 5th June, 2017
__description__	: To replace line in a text file
'''
def lineReplace( fileName, lineNumber, str):
	'''Function to replace a line in file
	
	Input arguments:
	filaName   : Name of the file
	lineNumber : Number of line to be replaced(int)
	str	   : String to write into file
	
	Output:
	None 
	'''
	# Reading file content in variable
	file = open( fileName, 'r')
	data = file.readlines()
	file.seek(0)
	
	# Altering content 	
	data[lineNumber-1] = str +'\n'
	
	# Writing into file
	file = open( fileName, 'w')
	file.writelines(data)
	file.close()
	return 
	
def main():
	# Replacing first five lines in file
	for i in range(1,6):
		lineReplace('data.txt',i,'Divya')

if __name__ == '__main__':
	main()
