from chord import *
from getKey import currentKey, pitches, major, minor

def main():
	print 'hello world'
	#getSeventh(currentKey[0])

def getIndex(key):
	for i in range(len(pitches)):
		if major[i] == key or minor[i] == key:
			return i

def getMinorSeventh(tonic):
	print 'the tonic of this chord is ' + tonic

def getSeventh(tonic):
	seventhChord = chord(currentKey[5], currentKey[3], currentKey[1], currentKey[6])
	print seventhChord.soprano
	print seventhChord.alto
	print seventhChord.tenor
	print seventhChord.bass
	getMinorSeventh(pitches[getIndex(tonic)-1])

if __name__ == '__main__':
	main()