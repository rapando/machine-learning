import re

class NK():
	def __init__(self):
		self.K = 1
		self.N = 0
		self.binary = ""

		

		while True:
			self.binary = input ("\nEnter a binary string : ")
			if len(self.binary) > 3 and self.validate(self.binary) == True:
				self.N = len (self.binary)
				break
			else:
				print ("The string must be made of 1 and 0 and more than 3 characters")

		print ("The value of N is {} and K is {}". format(self.N, self.K))



	def f (self, values):
		first = int (values[0])
		second = int (values[1])
		if   first == 0 and second == 0 : 
			return 0
		elif first == 0 and second == 1 : 
			return 1
		elif first == 1 and second == 0 : 
			return 2
		else : 
			return 0

	def fitness (self):
		totalFitness = 0
		print ("\nGetting the fitness\n")

		for i in range (self.N):
			if (i == self.N -1):
				values = [self.binary[i], self.binary[0]]
			else:
				values = [ self.binary[i], self.binary[i+1]]

			currentFitness = self.f(values) 
			print ("Fitness f({},{}) = {}" . format(values[0], values[1], currentFitness))
			totalFitness += currentFitness

		print ("\nThe total fitness is ", totalFitness)

	def validate(self, strg, search=re.compile(r'[^1 0]').search):
		return not bool(search(strg))



nk = NK()
nk.fitness()


