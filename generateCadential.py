"""
generates chord tones for a cadential 6/4
"""

from getKey import currentKey
from chord import *

def generateCad(tonic):
	"""
	parameters
	----------
		tonic : str
			the tonic key
	"""
	chord1 = Chord(currentKey[0], currentKey[4], currentKey[2], currentKey[4])
	chord2 = Chord(currentKey[6], currentKey[4], currentKey[1], currentKey[4])
	chord3 = Chord(currentKey[0], currentKey[4], currentKey[0], currentKey[0])
	print('\nhere\'s your cadential 6/4 in the key of ' + tonic + '!\n')
	printChords(chord1, chord2, chord3)

def printChords(chord_a, chord_b, chord_c):
	"""prints four voices of each chord in cadential 6/4 progression

	parameters
	----------
		chord_a : Chord object
			the V 6/4 chord
		chord_b : Chord object
			the V 5/3 chord
		chord_c : Chord object
			the I chord
	"""
	print('', chord_a.soprano, ' ', chord_b.soprano, '  ', chord_c.soprano)
	print('', chord_a.alto, ' ', chord_b.alto, '  ', chord_c.alto)
	print('', chord_a.tenor, ' ', chord_b.tenor, '  ', chord_c.tenor)
	print('', chord_a.bass, ' ', chord_b.bass, '  ', chord_c.bass)
	print('\n[6 - 5]')
	print('[4 - 3]')
	print('   V      I')