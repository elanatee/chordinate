from getKey import currentKey
from chord import *

def generateCad(tonic):
	chord1 = chord(currentKey[0], currentKey[4], currentKey[2], currentKey[4])
	chord2 = chord(currentKey[6], currentKey[4], currentKey[1], currentKey[4])
	chord3 = chord(currentKey[0], currentKey[4], currentKey[0], currentKey[0])
	print ''
	print 'here\'s your cadential 6/4!'
	printChords(chord1, chord2, chord3)

def printChords(chord_a, chord_b, chord_c):
	print '\n', '', chord_a.soprano, ' ', chord_b.soprano, '  ', chord_c.soprano
	print '', chord_a.alto, ' ', chord_b.alto, '  ', chord_c.alto
	print '', chord_a.tenor, ' ', chord_b.tenor, '  ', chord_c.tenor
	print '', chord_a.bass, ' ', chord_b.bass, '  ', chord_c.bass
	print '\n[6 - 5]'
	print '[4 - 3]'
	print '   V      I'