# A happy prime is a number that is both happy and prime. 
# Write the function nthHappyPrime(n) which takes a non-negative integer 
# and returns the nth happy prime number (where the 0th happy prime number is 7).




def numSquareSum(n):
    squareSum = 0
    while(n):
        squareSum += (n % 10) * (n % 10)
        n = int(n / 10)
    return squareSum
 

def isHappynumber(n):
    slow = n
    fast = n
    while(True):
         
        # move slow number
        # by one iteration
        slow = numSquareSum(slow)
 
        # move fast number
        # by two iteration
        fast = numSquareSum(numSquareSum(fast))
        if(slow != fast):
            continue
        else:
            break
 
    # if both number meet at 1,
    # then return true
    return (slow == 1)

# print(isHappynumber(10))

def fun_nth_happy_prime(n):
	n = n + 2
	i = 0
	while n > 0:
		if isHappynumber(i):
			n = n - 1
		i = i + 1
	return i - 1

print(fun_nth_happy_prime(0))