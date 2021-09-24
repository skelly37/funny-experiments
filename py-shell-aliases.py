from os import system as s

class Clear():
	def __repr__(self):
		s("clear")
		return ""

class Exit():
	def __repr__(self):
		exit()

class rand():
	def __init__(self, start, end):
		self.start = start
		self.end = end

	def __repr__(self):
		from random import randint
		return str(randint(self.start, self.end))

_ = Clear()
e = Exit()
