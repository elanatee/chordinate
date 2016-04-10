from getKey import *
from generateCadential import *

def main():
	prompt = raw_input('\nwhat would you like to do? \n1) generate cadential 6/4\n')
	if prompt == '1':
		key = getKey()
		if key:
			#print 'valid key!'
			generateCad(key)
	else:
		print 'that is not an option! try again'
		main()

if __name__ == '__main__':
	main()