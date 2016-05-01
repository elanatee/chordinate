from chord import *
from getKey import currentKey, pitches, major, minor
from random import randint

def getIndex(key):
	for i in range(len(pitches)):
		if major[i] == key or minor[i] == key:
			return i

def getDiminishedSeventh(tonic):
	#print 'the tonic of this chord is ' + tonic
	#print 'the diminished seventh of this chord is ' + pitches[getIndex(tonic)-3]
	return pitches[getIndex(tonic)-3]

# input: tonic of chord
# returns: third or fifth of chord
def random(chordTonic):
	#print currentKey
	#print 'the tonic of this chord is', chordTonic
	#print getIndex(chordTonic)
	num = randint(0,11)	# random number between 0-10
	#print 'num is ' + str(num)
	if num < 5:
		return minor[(getIndex(chordTonic) + 3) % len(minor)].upper() # third of chord - 3 half steps up from chord tonic
	else:
		return minor[(getIndex(chordTonic) + 6) % len(minor)].upper() # fifth of chord - 6 half steps up from chord tonic

# super duper hacky way of undoing capitalization of the flat symbol (b) wow
def capitalize(note):
	if len(note) > 1: 
		if note[1] == 'B':
			note = note[:-1]
			note += 'b'
	return note

def getSeventh(tonic):
	root = currentKey[6]
	seventhChord = chord(getDiminishedSeventh(pitches[getIndex(tonic)-1]), None, None, root)
	
	# there should be a better way to do this
	altoVoice = capitalize(random(root))
	seventhChord.setAlto(altoVoice) # randomly set alto to third or fifth

	if seventhChord.alto == minor[(getIndex(root) + 3) % len(minor)].upper(): # if alto is third
		tenorVoice = capitalize(minor[(getIndex(root) + 6) % len(minor)].upper())
		seventhChord.setTenor(tenorVoice) # tenor should be fifth
	else:
		tenorVoice = capitalize(minor[(getIndex(root) + 3) % len(minor)].upper())
		seventhChord.setTenor(tenorVoice)

	print seventhChord.soprano
	print seventhChord.alto
	print seventhChord.tenor
	print seventhChord.bass

	return seventhChord

def resolveToI(sevenChord):
	# TO DO: actually make this work
	# assumption: root is on bottom and seventh is on top
	# thus, third of chord must resolve to third of I chord b/c always below 7th
	chordTonic = sevenChord.getBass()
	oneChord = chord(currentKey[4], currentKey[0], currentKey[0], currentKey[0])
	thirdOfChord = minor[(getIndex(chordTonic) + 3) % len(minor)].upper()
	fifthOfChord = minor[(getIndex(chordTonic) + 6) % len(minor)].upper()
	if sevenChord.getTenor() == fifthOfChord: 
		oneChord.setTenor(currentKey[2])
		oneChord.setAlto(currentKey[2])
	return oneChord
	
def test(oneChord, soprano, alto, tenor, bass):
	# check if answer is correct here
	print 'test called'
	#print soprano
	#print oneChord.soprano
	if (soprano == oneChord.soprano) and (alto == oneChord.alto) and (tenor == oneChord.tenor) and (bass == oneChord.bass):
		print 'correct!'
	else:
		print 'incorrect :('
