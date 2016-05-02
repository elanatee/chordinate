from getKey import *
from fullyDiminishedSevenths import *
from generateCadential import *

def main():
	print 'welcome to chordinate!'
	showPrompt()

def showPrompt():
	prompt = raw_input('\nwhat would you like to do? \n1) generate cadential 6/4\n2) practice fully diminished sevenths\n')
	if prompt == '1':
		key = getKey()
		if key:
			#print 'valid key!'
			generateCad(key)
	elif prompt == '2':
		key = getKey()
		if key:
			print '\nresolve the following viio7 chord to the appropriate I chord:\n'
			sevenChord = getSeventh(key)
			oneChord = resolveToI(sevenChord)
			#oneChord.printChord()

			sevenChord.printChord()
			soprano = raw_input('soprano: ')
			alto = raw_input('alto: ')
			tenor = raw_input('tenor: ')
			bass = raw_input('bass: ')
			test(oneChord, soprano, alto, tenor, bass)
	else:
		print 'that is not an option! try again'
		showPrompt()

if __name__ == '__main__':
	main()