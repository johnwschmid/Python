class mathdojo(object):
	def __init__(self):
		self.count = 0

	def add(self, *args, **kwargs):
		for x in args:
			if type(x) is int:
				self.count += x
		for x in args:
			if type(x) is list:
				for i in x:
					self.count += i
		for x in args:
			if type(x) is tuple:
				for i in x:
					self.count += i
		return self

	def subtract(self, *args, **kwargs):
		for x in args:
			if type(x) is int:	
				self.count -= x
		for x in args:
			if type(x) is list:
				for i in x:
					self.count -= i
		for x in args:
			if type(x) is tuple:
				for i in x:
					self.count -= i
		return self

	def result(self):
		print "Count: " + str(self.count)


md = mathdojo()

md.add([3], 4, 5).subtract(2,3).add([4,6,7]).subtract(2,[1.4,7.8]).result()