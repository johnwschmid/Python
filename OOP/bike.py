class bike(object):
	def __init__(self, price, speed):
		self.price = price
		self.speed = speed
		self.miles = 0

	def displayinfo(self):
		print 'Price: $' + str(self.price)
		print 'Max Speed:' + str(self.speed)
		print 'Total Miles:' + str(self.miles)
		return self

	def ride(self):
		print 'Riding'
		self.miles += 10
		return self

	def reverse(self):
		print 'Reversing'
		if self.miles > 5:
			self.miles -= 5
		return self

GXR = bike(250,180)

GXR.ride().ride().displayinfo()