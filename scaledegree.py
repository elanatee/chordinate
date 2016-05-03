CM = ['C','D','E','F','G','A','B']

def getScaleDegree():
	degree = raw_input('enter a scale degree: ')
	degree = int(degree)
	print 'the ' + str(degree) + ' scale degree is ' + str(CM[degree-1])

#def getBebopScale(key):


key = raw_input('enter a key: ')
if key == 'C':
	choice = raw_input('what would you like to do? 1) get scale degree, 2) get scales ')
	choice = int(choice)
	if choice == 1:
		getScaleDegree()
	elif choice == 2:
		scaleType = raw_input('which scale would you like? 1) major, 2) minor bebop ')
		scaleType = int(scaleType)
		if scaleType == 1:
			print CM
		elif scaleType == 2:
			getBebopScale()