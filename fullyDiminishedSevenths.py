"""
generates fully diminished seventh chords, 
prompts user to enter notes to resolve viio7 to I chord in SATB style, 
and checks if input is correct
"""

from chord import *
from getKey import *
from random import randint


def getIndex(note):
	"""finds the index of a note in a list of pitches

	parameters
	----------
		note : str
			the name of a note

	returns
	-------
		index : int
			the index of a pitch in either pitches or pitches_sharp
	"""
	for index in range(len(pitches)):
		if pitches[index] == note or pitches_sharp[index] == note:
			return index

def getDiminishedSeventh(tonic):
	"""
	parameters
	----------
		tonic : str

	returns
	-------
		d7 : str
			diminished seventh of a key/chord
	"""
	d7 = pitches[getIndex(tonic)-3]
	return d7

def random(chordTonic):
	"""
	parameters
	----------
		chordTonic : str
	
	returns
	-------
		either the third or fifth of a chord
	"""	
	# random number between 0-10
	num = randint(0,11)	

	if chordTonic in pitches:
		if num < 5:	
			# third of chord - 3 half steps up from chord tonic
			return pitches[(getIndex(chordTonic) + 3) % len(minor)].upper() 
		else:
			# fifth of chord - 6 half steps up from chord tonic
			return pitches[(getIndex(chordTonic) + 6) % len(minor)].upper() 
	elif chordTonic in pitches_sharp:
		if num < 5:
			# third of chord - 3 half steps up from chord tonic
			return pitches_sharp[(getIndex(chordTonic) + 3) % len(minor)].upper() 
		else:
			# fifth of chord - 6 half steps up from chord tonic
			return pitches_sharp[(getIndex(chordTonic) + 6) % len(minor)].upper() 

def capitalize(note):
	"""super duper hacky way of undoing capitalization of the flat symbol (b) w0w
	
	parameters
	----------
		note : str
			the name of a note that may need flat symbol, e.g. "C" or "AB"

	returns
	-------
		note : str
			capitalized note with lowercase b to indicate flat note
	"""
	if len(note) > 1: 
		if note[1] == 'B':
			note = note[:-1]
			note += 'b'
	return note

def keyHasSharps(tonic):
	"""
	parameters
	----------
		tonic : str

	returns
	-------
		hasSharps : bool 
			True if a key has sharps
	"""
	hasSharps = False
	if tonic in sharp_keys:
		hasSharps = True
	return hasSharps

def getLeadingTone(keyTonic):
	"""
	parameters
	----------
		keyTonic : str

	returns
	-------
		leading : str
			raised leading tone of a key
	"""
	leading = pitches_sharp[getIndex(keyTonic.upper())-1]
	return leading

def getSeven(tonic):
	"""generates the fully diminished vii chord 
	
	parameters
	----------
		tonic : str
			tonic of a key
	returns
	-------
		sevenChord : Chord object
			the fully diminished vii chord
	"""
	root = currentKey[6]

	if tonic in major:
		# chord is built off scale degree 7 
		rootOfChord = root 
	elif tonic in minor:
		# chord is built off leading tone
		rootOfChord = getLeadingTone(tonic)

	# sets the seventh to diminished seventh and root to rootOfChord
	## if key with flats
	if tonic in pitches: 
		tonicIndex = getIndex(capitalize(tonic.upper()))
		diminishedSeventh = getDiminishedSeventh(pitches[tonicIndex-1])
		if tonic in major:
			sevenChord = Chord(diminishedSeventh, None, None, rootOfChord)
		elif tonic in minor: 
			sevenChord = Chord(diminishedSeventh, None, None, rootOfChord)

	## if key with sharps
	else:
		tonicIndex = getIndex(capitalize(tonic.upper()))
		diminishedSeventh = getDiminishedSeventh(pitches_sharp[tonicIndex-1])
		if tonic in major:
			sevenChord = Chord(diminishedSeventh, None, None, rootOfChord)
		elif tonic in minor:
			sevenChord = Chord(diminishedSeventh, None, None, rootOfChord)

	# sets third and fifth of chord
	# there's a better way to do this prob
	altoVoice = capitalize(random(rootOfChord))
	sevenChord.setAlto(altoVoice) # randomly set alto voice to third or fifth

	if sevenChord.alto == minor[(getIndex(rootOfChord) + 3) % len(minor)].upper(): # if alto is third
		tenorVoice = capitalize(minor[(getIndex(rootOfChord) + 6) % len(minor)].upper())
		sevenChord.setTenor(tenorVoice) # tenor should be fifth
	else:
		tenorVoice = capitalize(minor[(getIndex(rootOfChord) + 3) % len(minor)].upper())
		sevenChord.setTenor(tenorVoice)

	return sevenChord


def resolveToI(sevenChord):
	"""generates I chord based on rules for resolving root, third, fifth, seventh

	parameters
	----------
		sevenChord : Chord object
			the fully diminished vii chord
	
	returns
	-------
		oneChord : Chord object
			the I chord viio7 resolves to
	"""
	# assumption: root is on bottom and seventh is on top
	# thus, third of chord must resolve to third of I chord b/c always below 7th
	chordTonic = sevenChord.getBass()
	oneChord = Chord(currentKey[4], None, None, currentKey[0])
	thirdOfChord = minor[(getIndex(chordTonic) + 3) % len(minor)].upper()
	fifthOfChord = minor[(getIndex(chordTonic) + 6) % len(minor)].upper()

	if sevenChord.getTenor() == fifthOfChord: 
		oneChord.setTenor(currentKey[2])
		oneChord.setAlto(currentKey[2])
	else:
		oneChord.setTenor(currentKey[2])
		oneChord.setAlto(currentKey[2])

	return oneChord

def test(oneChord, soprano, alto, tenor, bass):
	"""checks if inputted answer is same as generated I chord

	parameters
	----------
		oneChord : Chord object
			the I chord with correct voices
		soprano : str
			user guess for soprano voice
		alto : str
			user guess for alto voice
		tenor : str 
			user guess for tenor voice
		bass : str 
			user guess for bass voice
	
	returns 
	-------

	"""
	userCorrect = False
	if (soprano == oneChord.soprano) and (alto == oneChord.alto) and (tenor == oneChord.tenor) and (bass == oneChord.bass):
		userCorrect = True
		print('\ncorrect!')
	else:
		print('\nincorrect :(')
	return userCorrect
