from getKey import *

choice = input('what would you like to do? 1) get scale degree, 2) get scales ')
if choice == 1:
	getScaleDegree()
elif choice == 2:
	scaleType = input('which scale would you like? 1) major, 2) minor bebop ')
	if scaleType == 1:
		print CM
	elif scaleType == 2:
		getBebopScale()