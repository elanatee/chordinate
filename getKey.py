pitches = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
minor = ['c', 'c#', 'd', 'eb', 'e', 'f', 'f#', 'g', 'g#', 'a', 'bb', 'b']
major = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']
currentKey = []

def main():
	getKey()
	"""
	keyPitches = ""
	for i in currentKey:
		keyPitches += i + " "
	print keyPitches
	"""

"""
returns the index of a pitch in array of major/minor notes
"""
def getIndex(key):
	for i in range(len(pitches)):
		if major[i] == key or minor[i] == key:
			return i

def halfStep(pitch):
	return pitch + 1

def wholeStep(pitch):
	return pitch + 2

"""
sets currentKey to be a major key
"""
def getMajor(tonic):
	index = getIndex(tonic)
	for i in range(7):
		#print pitches[index]
		currentKey.append(pitches[index % len(pitches)])
		if i == 2:
			index = halfStep(index)
		else:
			index = wholeStep(index)

"""
sets currentKey to be a minor key
"""
def getMinor(tonic):
	index = getIndex(tonic)
	for i in range(7):
		currentKey.append(pitches[index % len(pitches)])
		if i == 1 or i == 4:
			index = halfStep(index)
		else:
			index = wholeStep(index)

"""
prompts users to enter name of key
returns key or prompts again for valid key name 
"""
def getKey():
	# need to clear the current key first
	# otherwise currentKey will grow indefinitely
	del currentKey[:]
	key = raw_input('\nenter a key: ')
	#print 'you chose the key of ' + key 
	if key in major:
		getMajor(key)
		return key
	elif key in minor:
		getMinor(key)
		return key
	else:
		print 'please enter a valid key'
	
if __name__ == '__main__':
	main()