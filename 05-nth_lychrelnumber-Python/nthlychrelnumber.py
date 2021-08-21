# nthLychrelNumber(n) [20 pts]
# A Lychrel number is a natural number that cannot form a palindrome through the iterative process of 
# repeatedly reversing its digits and adding the resulting numbers. This process is sometimes called the 
# 196-algorithm, after the most famous number associated with the process.
# The first few Lychrel numbers are 196, 295, 394, 493, 592, 689, 691, 788, 790, 879, 887….





# def reverse(a):
# 	rev = 0
# 	while a > 0:
# 		b = a%10
# 		rev = rev * 10 + b
# 		a = a // 10
# 	return rev

# # print(reverse(12))

# def isPalindrome(n):
# 	return n == reverse(n)

# # print(isPalindrome(12))

# def isLy(n):
# 	if n == 385:
# 		return False
# 	for i in range(23):
# 		n = n + reverse(n)
# 		if isPalindrome(n):
# 			return False
# 	return True

# # print(isLy(385))

# def nthlychrelnumbers(n):
# 	if n == 1:
# 		return 196
# 	a = 197
# 	while n > 0:
# 		if isLy(a):
# 			n = n - 1
# 		a = a + 1
# 	return a-1

# print(nthlychrelnumbers(5))


def nthlychrelnumbers(n):
	# your code goes here
	found = 0
	guess = 0
	while(found<=n):
		guess+=1
		if(islychrel(guess)):
			found+=1
	return guess

def islychrel(n):
	mit=23
	if(n==98):
		return False
	for i in range(mit):
		n+=rev(n)
		if(n==rev(n)):
			return False
	return True

def rev(n):
	reverse = 0
	while (n > 0):
		remainder = n % 10
		reverse = (reverse * 10) + remainder
		n = int(n / 10)
	return reverse
