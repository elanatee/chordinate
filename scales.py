from getKey import *

"""
UNFINISHED
"""

def main():
	getScales()

def getScales():
	scaleType = input('which scale would you like? 1) major, 2) minor, 3) minor bebop\n')
	if scaleType == 1:
		getKey()
		print currentKey

if __name__ == '__main__':
	main()