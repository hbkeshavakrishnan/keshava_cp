# nthAutomorphicNumbers(n) [20 pts]
# In mathematics, an automorphic number is a number whose square "ends" in the same digits as the 
# number itself. For example, 5^2 = 25, 6^2 = 36, 76^2 = 5776, and 890625^2 = 793212890625, so 5, 6, 
# 76 and 890625 are all automorphic numbers.


def count(n):
	c = 0
	while n > 0:
		n = n // 10
		c = c + 1
	return c

# # print(count(6))

def auto(n):
	a = n*n
	b = count(n)
	c = a % (10 ** b)
	return c == n

# # print(auto(890625))

def nthautomorphicnumbers(n):
	if n == 1:
		return 0
	if n == 2:
		return 1
	i = 0
	while n > 0:
		if auto(i):
			n = n - 1
		i = i + 1

	return i-1


# print(nthautomorphicnumbers(28))




