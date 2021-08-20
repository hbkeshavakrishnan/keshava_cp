# nthPowerfulNumber(n) [20 pts]
# Write the function nthPowerfulNumber(n). See here for details. So nthPowerfulNumber(0) returns 
# 1, and nthPowerfulNumber(10) returns 64.
# A number n is said to be Powerful Number if for every prime factor p of it, p2 also divides it. 
# For example:- 36 is a powerful number. It is divisible by both 3 and square of 3 i.e, 9.


import math

def isPowerFulNumber(a):
	while a%2 == 0:
		power = 0
		while a%2 == 0:
			a = a//2
			power = power + 1
		if power == 1:
			return False
	for factor in range(3, int(math.sqrt(a))+1, 2):
		power = 0
		while (a % factor == 0):
			a = a // factor
			power = power + 1
		if power == 1:
			return False
	return a == 1

# print(isPowerFulNumber(8))


def nthpowerfulnumber(n):
	i = 1
	n = n + 1
	while n > 0:
		if isPowerFulNumber(i):
			n = n - 1
		i = i + 1
	return i - 1

print(nthpowerfulnumber(10))