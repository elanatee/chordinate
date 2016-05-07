from getKey import *
from fullyDiminishedSevenths import *
from generateCadential import *

def main():
	print 'welcome to chordinate!'
	showPrompt()

def cadential():
	key = getKey()
	if key:
		#print 'valid key!'
		generateCad(key)
	else:
		cadential()

def testFullyDiminished():
	key = getKey()
	if key:	
		#print 'currentkey is', currentKey
		print '\nresolve the following viio7 chord to the appropriate I chord in the key of ' + key + ':\n'
		
		def getInput():
			sevenChord = getSeventh(key)
			oneChord = resolveToI(sevenChord)
			#oneChord.printChord()

			sevenChord.printChord()

			soprano = raw_input('\nsoprano: ')
			alto = raw_input('alto: ')
			tenor = raw_input('tenor: ')
			bass = raw_input('bass: ')
			correctAnswer = test(oneChord, soprano, alto, tenor, bass)

			if correctAnswer is False:
				retry = raw_input('\ntry again? (y/n) ')
				if retry == 'y':
					getInput()
				elif retry == 'n':
					return
				else: 
					print 'okay bye'

		getInput()

	else: 
		testFullyDiminished()

def showPrompt():
	prompt = raw_input('\nwhat would you like to do? \n1) generate cadential 6/4\n2) practice fully diminished sevenths \n3) exit\n\n')

	if prompt == '1': 
		cadential()
		showPrompt()
	elif prompt == '2':
		testFullyDiminished()
		showPrompt()
	elif prompt == '3': 
		print 'okay, goodbye!'
		return
	else:
		print 'that is not an option! try again'
		showPrompt()

if __name__ == '__main__':
	main()