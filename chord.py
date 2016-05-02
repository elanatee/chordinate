class chord:

	def __init__(self, soprano, alto, tenor, bass):
		self.soprano = soprano
		self.alto = alto
		self.tenor = tenor
		self.bass = bass

	def printChord(self):
		print self.soprano
		print self.alto
		print self.tenor
		print self.bass

	def setSoprano(self, pitch):
		self.soprano = pitch

	def setAlto(self, pitch):
		self.alto = pitch

	def setTenor(self, pitch):
		self.tenor = pitch

	def setBass(self, pitch):
		self.bass = pitch

	def getTenor(self):
		return self.tenor

	def getAlto(self):
		return self.alto

	def getBass(self):
		return self.bass