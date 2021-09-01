# Happy Primes [20 pts]
# Background: read the first paragraph from the Wikipedia page on happy numbers. After 
# some thought, we see that no matter what number we start with, when we keep replacing 
# the number by the sum of the squares of its digits, we'll always either arrive at 4 (
# unhappy) or at 1 (happy). With that in mind, we want to write the function nthHappyNumber
# (n). However, to write that function, we'll first need to write isHappyNumber(n) (
# right?). And to write that function, we'll first need to write sumOfSquaresOfDigits(n). 
# And that's top-down design! Here we go.... 
# Note: the autograder will grade each of the following functions, so they are required. 
# However, they also are here specifically because they are just the right helper 
# functions to make nthHappyNumber(n) easier to write!

def ishappyprimenumber(n):
    # Your code goes here
    if((isHappynumber(n)) and isPrime(n)):
        return True
    return False

def isHappynumber(n): 
	slow = n
	fast = n
	while(True):  
		slow = numSquareSum(slow)
		fast = numSquareSum(numSquareSum(fast))
		if(slow != fast): 
			continue
		else: 
			break
	return (slow == 1)

def numSquareSum(n): 
	squareSum = 0
	while(n): 
		squareSum += (n % 10) * (n % 10)
		n = int(n / 10)
	return squareSum

def isPrime(n):
    if(n<2):
        return False
    for i in range(2,n):
        if(n%i==0):
            return False
    return True