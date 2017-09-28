"""
returns scale degrees for major and minor keys according to user input
"""

pitches = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B']
pitches_sharp = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']

minor = ['c', 'c#', 'd', 'eb', 'e', 'f', 'f#', 'g', 'g#', 'a', 'bb', 'b']
major = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'F#', 'G', 'Ab', 'A', 'Bb', 'B']

sharp_keys = ['G', 'D', 'A', 'E', 'B', 'F#', 'e', 'b', 'f#', 'c#', 'g#', 'd#', 'a#']

currentKey = []

def main():
	getKey()
	
def getIndex(key):
	"""
	returns
	-------
		index : int
			the index of a pitch in array of major/minor notes
	"""
	for index in range(len(pitches)):
		if major[index] == key or minor[index] == key:
			return index

def halfStep(pitch):
	return pitch + 1

def wholeStep(pitch):
	return pitch + 2

def keyHasSharps(tonic):
	if tonic in sharp_keys:
		return True
	else:
		return False

def getMajor(tonic):
	"""initializes currentKey with pitches of major key

	parameters
	----------
		tonic : str
	"""
	index = getIndex(tonic)
	for i in range(7):
		#print pitches[index]
		# this should make things have proper enharmonic spelling
		if keyHasSharps(tonic):
			currentKey.append(pitches_sharp[index % len(pitches)])
		else:
			currentKey.append(pitches[index % len(pitches)])

		if i == 2:
			index = halfStep(index)
		else:
			index = wholeStep(index)

def getMinor(tonic):
	"""initializes currentKey with pitches of minor key

	parameters
	----------
		tonic : str
	"""
	index = getIndex(tonic)
	for i in range(7):
		if keyHasSharps(tonic):
			currentKey.append(pitches_sharp[index % len(pitches)])
		else:
			currentKey.append(pitches[index % len(pitches)])
		if i == 1 or i == 4:
			index = halfStep(index)
		else:
			index = wholeStep(index)

def getKey():
	"""prompts users to enter name of key
	
	if valid key, sets currentKey and returns key
	otherwise, prompts for valid key
	"""
	# clear currentKey first, 
	# otherwise currentKey will grow indefinitely
	del currentKey[:]

	key = input('\nenter a key (uppercase for major, lowercase for minor): ')

	if key in major:
		getMajor(key)
		return key
	elif key in minor:
		getMinor(key)
		return key
	else:
		print('please enter a valid key')
	
if __name__ == '__main__':
	main()