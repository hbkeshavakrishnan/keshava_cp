# Note: please do not start this problem prior to completing previous problem. 
# Bearing in mind the definition of Kaprekar Number from above problem, write the function 
# nearestKaprekarNumber(n) that takes an int value n and returns the Kaprekar number 
# closest to n, with ties going to smaller value. For example, nearestKaprekarNumber(49) returns 45, 
# and nearestKaprekarNumber(51) returns 55. And since ties go to the smaller number, 
# nearestKaprekarNumber(50) returns 45. 
# Note: as you probably guessed, this also cannot be solved by counting up from 0, 
# as that will not be efficient enough to get past the autograder. 
# Hint: one way to solve this is to start at n and grow in each direction until you find a Kaprekar number.



import math


def count(n):
    c = 0
    while n > 0:
        c += 1
        n = n // 10
    return c


def kap(n):
    z = n ** 2
    a = count(z)
    for i in range(1, a+1):
        b = z % (10 ** i)
        c = z // (10 ** i)
        # print(b,c)
        if n == b + c:
            return True
    return False

# print(kap(297))





def fun_nearestkaprekarnumber(n):
    i = 1
    a = True
    while a:
        b = n - i
        c = n + i
        if kap(n):
            a = False
            return n
        if kap(b):
            a = False
            return b
        if kap(c):
            a = False
            return c
        i += 1
    return 1

# print(fun_nearestkaprekarnumber(3861))