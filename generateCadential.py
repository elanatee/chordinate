from getKey import currentKey
from chord import *

def generateCad(tonic):
	chord1 = chord(currentKey[0], currentKey[4], currentKey[2], currentKey[4])
	chord2 = chord(currentKey[6], currentKey[4], currentKey[1], currentKey[4])
	print ''
	print 'here\'s your cadential 6/4!'
	printChords(chord1, chord2)

def printChords(chord_a, chord_b):
	print '\n', '', chord_a.soprano, ' ', chord_b.soprano
	print '', chord_a.alto, ' ', chord_b.alto
	print '', chord_a.tenor, ' ', chord_b.tenor
	print '', chord_a.bass, ' ', chord_b.bass
	print '\n[6 - 5]'
	print '[4 - 3]'
	print '   V'