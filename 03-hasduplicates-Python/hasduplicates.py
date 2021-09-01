# hasDuplicates(L) [15 pts]
# Write the function hasDuplicates(L) that takes a 2d list L of arbitrary values, and returns True if L 
# contains any duplicate values (that is, 
# if any two values in L are equal to each other), and False otherwise.

def hasduplicates(L):
	# Your code goes here
	l=[]
	for i in range(len(L)):
		for j in range(len(L[i])):
			l.append(L[i][j])
	l.sort()
	for i in range(len(l)-1):
		if(l[i]==l[i+1]):
			return True
	return False