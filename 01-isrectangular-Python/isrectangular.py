# Write the function isrectangular(L) that takes a possibly-2d 
# list L and returns True  if it is rectangular, so each row has
#  the same number of elements. Return False otherwise.


def fun_isrectangular(l):
	# Your code goes here...
	lr=len(l)
	for i in range(1,lr):
		if len(l[i])!=len(l[i-1]):
			return False
	return True



