a = [2,4,10,16]
def multi(array):
	for i in range(len(array)):
		array[i] = array[i] * 5
	return array

b = multi(a)
print b