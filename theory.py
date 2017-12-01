#! /usr/bin/env python
"""
main program flow
"""
from getKey import *
from fullyDiminishedSevenths import *
from generateCadential import *

def cadential():
	"""
	generates cadential 6/4 progression based on user input
	"""
	key = getKey()
	if key:
		generateCad(key)
	else:
		cadential()

def testFullyDiminished():
	"""
	tests user on viio7 chord resolution
	"""
	key = getKey()
	if key:	
		print('\nresolve the following viio7 chord to the appropriate I chord in SATB style:\n')
		
		def getInput():
			sevenChord = getSeven(key)
			oneChord = resolveToI(sevenChord)

			sevenChord.printChord()

			soprano = input('\nsoprano: ')
			alto = input('alto: ')
			tenor = input('tenor: ')
			bass = input('bass: ')

			correctAnswer = test(oneChord, soprano, alto, tenor, bass)

			if correctAnswer is False:
				retry = input('\ntry again? (y/n) ')
				if retry == 'y':
					getInput()
				elif retry == 'n':
					return
				else: 
					print('goodbye!')

		getInput()

	else: 
		testFullyDiminished()

def showPrompt():
	prompt = input('\nwhat would you like to do? \
						\n[1] generate cadential 6/4 \
						\n[2] practice resolving viio7 to I \
						\n[3] exit\n \
						\n> ')

	if prompt == '1': 
		cadential()
		showPrompt()
	elif prompt == '2':
		testFullyDiminished()
		showPrompt()
	elif prompt == '3': 
		return
	else:
		print('that is not an option! try again')
		showPrompt()

def main():
	print('\nwelcome to chordinate!')
	showPrompt()

if __name__ == '__main__':
	main()