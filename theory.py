from getKey import *
from fullyDiminishedSevenths import *
from generateCadential import *

def main():
	prompt = raw_input('\nwhat would you like to do? \n1) generate cadential 6/4\n2) practice fully diminished sevenths\n')
	if prompt == '1':
		key = getKey()
		if key:
			#print 'valid key!'
			generateCad(key)
	elif prompt == '2':
		key = getKey()
		if key:
			getSeventh(key)
	else:
		print 'that is not an option! try again'
		main()

if __name__ == '__main__':
	main()