pitches = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
currentKey = []

def main():
	key = raw_input('enter a key: ')
	#getKey(key)
	"""
	keyPitches = ""
	for i in currentKey:
		keyPitches += i + " "
	print keyPitches
	"""

def getIndex(key):
	for i in range(len(pitches)):
		if pitches[i] == key:
			return i

def halfStep(pitch):
	return pitch + 1

def wholeStep(pitch):
	return pitch + 2

def getKey():
	key = raw_input('\nenter a key: ')
	if key in pitches:
		#print 'you chose the key of ' + key 
		index = getIndex(key)
		for i in range(7):
			#print pitches[index]
			currentKey.append(pitches[index % len(pitches)])
			if i == 2:
				index = halfStep(index)
			else:
				index = wholeStep(index)
	else:
		print 'please enter a valid key'
		getKey()
	return key

if __name__ == '__main__':
	main()