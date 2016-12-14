class car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if (price > 10000):
			self.tax = '15%'
		else:
			self.tax = '12%'
		self.display()

	def display(self):
		print "Price: " + str(self.price)
		print "Top Speed: " + str(self.speed)
		print "Fuelage: " + str(self.fuel)
		print "Mileage: " + str(self.mileage)
		print "Tax: " + str(self.tax)
		print '\n'

Merc = car(35000, 220, 'Full', '25m/g')
Trashmobile = car(300,20,'Stupid Empty', '1m/g')