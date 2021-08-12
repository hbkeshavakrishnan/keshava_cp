# Write the function setKthDigit(n, k, d) that takes three integers -- n, k, and d 
# where n is a possibly-negative int, k is a non-negative int, and d is a non-negative 
# single digit (between 0 and 9 inclusive). This function returns the number n with 
# the kth digit replaced with d. Counting starts at 0 and goes right-to-left, 
# so the 0th digit is the rightmost digit. 



def fun_set_kth_digit(n, k, d):
		flag = 0
		if n < 0:
			flag = 1
			n = abs(n)
		a = []
		while n > 0:
			b = n%10
			a.append(b)
			n = n//10
		if len(a) <= k:
			a.append(d)
		else:
			a[k] = d
		res = 0
		for i in a[::-1]:
			res = res*10 + i
		if flag == 1:
			return -res
		return res

# print(fun_set_kth_digit(468,0,1))


