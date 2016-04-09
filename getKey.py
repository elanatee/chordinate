pitches = ['C','Db','D','Eb','E','F','Gb','G','Ab','A','Bb','B'] # size: 12
currentKey = []

def getIndex(key):
	for i in range(len(pitches)):
		if pitches[i] == key:
			return i

def getKey(key):
	if key in pitches:
		#print 'you chose the key of ' + key 
		index = getIndex(key)
		for i in range(7):
			#print pitches[index]
			currentKey.append(pitches[index % len(pitches)])
			if i == 2:
				index = index + 1
			else:
				index = index + 2
	else:
		print 'please enter a valid key'
		
if __name__ == '__main__':
	key = raw_input('enter a key: ')
	getKey(key)
	#print currentKey