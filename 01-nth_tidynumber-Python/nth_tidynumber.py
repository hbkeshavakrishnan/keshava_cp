# Write the function nthTidyNumber that takes a non-negative int n and returns the nth Tidy Number. 
# A tidy number is a number whose digits are in non-decreasing order.
# fun_nth_tidynumber(0) = 1
# fun_nth_tidynumber(1) = 2
# fun_nth_tidynumber(5) = 6
# fun_nth_tidynumber(15) = 17
# fun_nth_tidynumber(35) = 46
def digitCount(x):
	n=abs(x)
	c=0
	while(n>10):
		n=n//10
		c=c+1
	return (c+1)


def isTidy(n):
    d=digitCount(n)
    num=n
    for i in range(d):
        x=n%10
        n=int(n//10)
        p=n%10
        if(num<10):                     
            return True
        if((x==0) or (x<p)):
            return False
    return True

def fun_nth_tidynumber(n):
    n=abs(n)
    found = -1
    guess = 1
    while(found<n):
        
        if(isTidy(guess)):
            found+=1
        guess+=1
    return guess-1