'''
__author__ 	: Priyank Parmar
__tested_on__	: 
__description__ : To implement file operation like read and write
'''
import linecache

def main():
	# Line number user input
	line_num = raw_input('Enter Line number :')
	# Reading file line
	import linecache
	str = linecache.getline('data.txt',int(line_num))
	# Printing file line
	print str
	 

if __name__ ==  '__main__':
	main()
