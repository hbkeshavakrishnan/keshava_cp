# isMostlyMagicSquare(a) [15 pts]
# Write the function isMostlyMagicSquare(a) that takes an 2d list of numbers, which you may assume is an NxN square 
# with N>0, and returns True if it is "mostly magic" and False otherwise, where a square is "mostly magic" if:
# Each row, each column, and each of the 2 diagonals each sum to the same total.
# A completely magic square has additional restrictions (such as not allowing duplicates, and only allowing numbers 
# from 1 to N2), which we are not enforcing here, but which you can read about here. Note: any magic square is also 
# a "mostly magic" square, including this sample magic square:
# Read for more: https://en.wikipedia.org/wiki/Magic_square
# Here is another mostly-magic square:
# [ [ 42 ]]
# That square is 1x1 and each row, column, and diagonal sums to 42! And finally, here is a not-mostly-magic square:
# [ [ 1, 2],
#   [ 2, 1]]
# Each row and each column add to 3, but one diagonal adds to 2 and the other to 4.

def diagonal_cal(a):
	s = 0
	l = 0
	k = []
	for i in range(len(a)):
		s += a[i][i]
	k.append(s)
	for i in range(len(a)-1, -1, -1):
		l += a[i][i]
	k.append(l)
	return k

def row_cal(a):
	s = 0
	k = []
	for i in range(len(a)):
		for j in range(len(a[0])):
			s += a[i][j]
		k.append(s)
		s = 0
	return k

def col_cal(a):
	s = 0
	k = []
	for i in a:
		s += sum(i)
		k.append(s)
		s = 0
	return k

def ismostlymagicsquare(a):
	if len(a) != len(a[0]):
		return False
	k = row_cal(a)
	if len(k) == len(set(k)):
		return False
	l = col_cal(a)
	if len(l) == len(set(l)):
		return False
	b = diagonal_cal(a)
	if sum(row_cal(a)) == sum(col_cal(a)) == sum(b) + (b[0]) * (len(a) - 2):
		return True
	else:
		return False


print(col_cal([[16, 3, 2, 13], [5, 10, 11, 8], [9, 6, 7, 12],[4, 15, 14, 1]]))