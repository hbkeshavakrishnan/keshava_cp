def isPrime(n):
  if n == 0 or n == 1:
    return False
  for i in range(2, n):
    if n % i == 0:
      return False
  return True

# print(isPrime(9))1

def isPalindrome(n):
  a = str(n)
  return str(n) == a[::-1]


print(isPalindrome(101))