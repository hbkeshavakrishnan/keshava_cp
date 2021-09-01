# nthPronicNumber(n) [20 pts]
# Write the function nthPronicNumber that takes a non-negative int n and returns the nth Pronic 
# Number. Pronic number is a number which is the product of two consecutive integers, that is, a 
# number n is a product of x and (x+1).

def nthpronicnumber(n):
	# Your code goes here
	found=1
	guess=0
	while(found<=n):
		guess+=1
		if(isPronic(guess)):
			found+=1
	return guess

def isPronic(n):
	x=int(n**0.5)
	if(x*(x+1)==n):
		return True
	return False