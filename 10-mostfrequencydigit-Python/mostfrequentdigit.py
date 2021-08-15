# mostFrequentDigit(n) [10pts]
# Write the function mostFrequentDigit(n), that takes a non-negative integer n and returns the digit from 0 to 9 
# that occurs most frequently in it, with ties going to the smaller digit.

def mostfrequentdigit(n):
	if n == 0:
		return 0
	a = dict()
	while(n > 0):
		c = n % 10
		if c in a:
			a[c] += 1
		else:
			a[c] = 1
		n = n // 10
	m = max(a.values())
	k = []
	for i in a:
		if m == a[i]:
			k.append(i)
	return min(k)

	

print(mostfrequentdigit(5231123123123)) 
	