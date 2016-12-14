class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100

	def walk(self):
		print "Started walking."
		self.health -= 1
		return self

	def run(self):
		print "Now running."
		self.health -= 5
		return self

	def display(self):
		print "Health: " + str(self.health)

class Dog(Animal):
	def __init__(self,name):
		super(Dog, self).__init__(name)
		self.health = 150

	def pet(self):
		self.health += 5
		return self

class Dragon(Animal):
	def __init__(self,name):
		super(Dragon, self).__init__(name)
		self.health = 170

	def fly(self):
		self.health -= 10
		return self

	def display(self):
		super(Dragon, self).display()
		print "I am a dragon"


Scale = Dragon('Scale')

Scale.walk().run().fly().display()