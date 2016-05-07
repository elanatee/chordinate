from chord import *
from getKey import *
from random import randint

"""
input: key
returns: index of a pitch in either pitches or pitches_sharp
"""
def getIndex(key):
	for i in range(len(pitches)):
		if pitches[i] == key or pitches_sharp[i] == key:
			return i

"""
input: tonic of a chord
returns: diminished seventh of a key/chord
"""
def getDiminishedSeventh(tonic):
	#print 'the tonic of this chord is ' + tonic
	#print 'the diminished seventh of this chord is ' + pitches[getIndex(tonic)-3]
	return pitches[getIndex(tonic)-3]

"""
input: tonic of chord
returns: third or fifth of chord
"""
def random(chordTonic):
	#print 'the tonic of this chord is', chordTonic
	#print getIndex(chordTonic)

	num = randint(0,11)	# random number between 0-10
	#print 'num is ' + str(num)

	if chordTonic in pitches:
		if num < 5:
			return pitches[(getIndex(chordTonic) + 3) % len(minor)].upper() # third of chord - 3 half steps up from chord tonic
		else:
			return pitches[(getIndex(chordTonic) + 6) % len(minor)].upper() # fifth of chord - 6 half steps up from chord tonic
	elif chordTonic in pitches_sharp:
		if num < 5:
			return pitches_sharp[(getIndex(chordTonic) + 3) % len(minor)].upper() # third of chord - 3 half steps up from chord tonic
		else:
			return pitches_sharp[(getIndex(chordTonic) + 6) % len(minor)].upper() # fifth of chord - 6 half steps up from chord tonic

"""
super duper hacky way of undoing capitalization of the flat symbol (b) w0w
returns: capitalized note with lowercase b to indicate flat note
"""
def capitalize(note):
	if len(note) > 1: 
		if note[1] == 'B':
			note = note[:-1]
			note += 'b'
	return note

def keyHasSharps(tonic):
	sharp_keys = ['G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']
	if tonic in sharp_keys:
		return True
	else:
		return False

def getLeadingTone(keyTonic):
	##if keyHasSharps(keyTonic):
		return pitches_sharp[getIndex(keyTonic.upper())-1]
	##else:
	##	return pitches[getIndex(keyTonic.upper())-1]

"""
generates the seventh chord 
input: tonic of a key
returns: seventh chord object
"""
def getSeventh(tonic):
	root = currentKey[6]

	if tonic in major:
		rootOfChord = root
	elif tonic in minor:
		rootOfChord = getLeadingTone(tonic)

	#print 'tonic is', tonic

	# sets the seventh to diminished seventh and root to root
	## if key with flats
	if tonic in pitches: 
		if tonic in major:
			seventhChord = chord(getDiminishedSeventh(pitches[getIndex(capitalize(tonic.upper()))-1]), None, None, rootOfChord)
		elif tonic in minor: 
			seventhChord = chord(getDiminishedSeventh(pitches[getIndex(capitalize(tonic.upper()))-1]), None, None, rootOfChord)

	## if key with sharps
	else:
		if tonic in major:
			seventhChord = chord(getDiminishedSeventh(pitches_sharp[getIndex(capitalize(tonic.upper()))-1]), None, None, rootOfChord)
		elif tonic in minor:
			seventhChord = chord(getDiminishedSeventh(pitches_sharp[getIndex(capitalize(tonic.upper()))-1]), None, None, rootOfChord)

	# there's a better way to do this prob
	altoVoice = capitalize(random(rootOfChord))
	seventhChord.setAlto(altoVoice) # randomly set alto voice to third or fifth

	if seventhChord.alto == minor[(getIndex(rootOfChord) + 3) % len(minor)].upper(): # if alto is third
		tenorVoice = capitalize(minor[(getIndex(rootOfChord) + 6) % len(minor)].upper())
		seventhChord.setTenor(tenorVoice) # tenor should be fifth
	else:
		tenorVoice = capitalize(minor[(getIndex(rootOfChord) + 3) % len(minor)].upper())
		seventhChord.setTenor(tenorVoice)

	return seventhChord

"""
generates I chord based on rules for resolving root, third, fifth, seventh
input: seventh chord object
returns: one chord object
"""
def resolveToI(sevenChord):
	# assumption: root is on bottom and seventh is on top
	# thus, third of chord must resolve to third of I chord b/c always below 7th
	chordTonic = sevenChord.getBass()
	oneChord = chord(currentKey[4], None, None, currentKey[0])
	thirdOfChord = minor[(getIndex(chordTonic) + 3) % len(minor)].upper()
	fifthOfChord = minor[(getIndex(chordTonic) + 6) % len(minor)].upper()
	if sevenChord.getTenor() == fifthOfChord: 
		oneChord.setTenor(currentKey[2])
		oneChord.setAlto(currentKey[2])
	else:
		oneChord.setTenor(currentKey[2])
		oneChord.setAlto(currentKey[2])
	return oneChord

"""
checks if inputted answer is same as generated I chord
input: one chord and user inputted guesses for pitches
returns: true or false
"""
def test(oneChord, soprano, alto, tenor, bass):
	#print 'test called'
	if (soprano == oneChord.soprano) and (alto == oneChord.alto) and (tenor == oneChord.tenor) and (bass == oneChord.bass):
		print '\ncorrect!'
		return True
	else:
		print '\nincorrect :('
		return False
