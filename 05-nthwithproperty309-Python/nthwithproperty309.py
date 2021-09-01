# nthWithProperty309(n) [20 pts]
# We will say that a number n has "Property309" if its 5th power contains every 
# digit (from 0 to 9) at least once. 309 is the smallest number with this property. 
# Write the function nthWithProperty309 that takes a non-negative int n and returns 
# the nth number with Property309.

def nthwithproperty309(n):
	# Your code goes here
	found = 0
	guess = 308
	while(found<=n):
		guess+=1
		if(is309num(guess)):
			found+=1
	return guess

def is309num(n):
	l=['0','1','2','3','4','5','6','7','8','9']
	x=str(n**5)
	for i in range(len(l)):
		if(l[i] not in x):
			return False
	return True