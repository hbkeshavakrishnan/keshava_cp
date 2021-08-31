# median(a) (10 pts)
# Write the non-destructive function median(a) that takes a list of ints or floats and returns the median value, 
# which is the value of the middle element, or the average of the two middle elements if there is no single middle 
# element. If the list is empty, return None.

def median(a):
	# your code goes here
	if(len(a)==0):
		return None
	a.sort()
	if(len(a)%2==0):
		x=(a[len(a)//2]+a[(len(a)//2)-1])/2
	else:
		x=a[len(a)//2]
	return x