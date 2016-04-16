from chord import *
from getKey import currentKey, pitches, major, minor

def main():
	print 'hello world'
	#getSeventh(currentKey[0])

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
	num = 5	# this should be a random number between 0-10
	if num < 5:
		return minor[(getIndex(chordTonic) + 3) % len(minor)] # third of chord - 3 half steps up from chord tonic

	else:
		return minor[(getIndex(chordTonic) + 6) % len(minor)] # fifth of chord - 6 half steps up from chord tonic

def getSeventh(tonic):
	root = currentKey[6]
	seventhChord = chord(getDiminishedSeventh(pitches[getIndex(tonic)-1]), None, None, root)
	
	# there's a better way to do this /shrug
	seventhChord.setAlto(random(root)) # randomly set alto to third or fifth
	if seventhChord.alto == minor[(getIndex(root) + 3) % len(minor)]: # if alto is third
		seventhChord.setTenor(minor[(getIndex(root) + 6) % len(minor)]) # tenor should be fifth
	else:
		seventhChord.setTenor(minor[(getIndex(root) + 3) % len(minor)])

	print seventhChord.soprano
	print seventhChord.alto
	print seventhChord.tenor
	print seventhChord.bass

	return seventhChord

def resolveToI(sevenChord):
	# TO DO: actually make this work
	oneChord = chord(currentKey[0], currentKey[0], currentKey[0], currentKey[0])
	return oneChord
	
def test(oneChord, soprano, alto, tenor, bass):
	# check if answer is correct here
	print 'test called'
	print soprano
	print oneChord.soprano
	if (soprano == oneChord.soprano) and (alto == oneChord.alto) and (tenor == oneChord.tenor) and (bass == oneChord.bass):
		print 'correct!'
	else:
		print 'incorrect :('

if __name__ == '__main__':
	main()