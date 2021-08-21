# shortenLongRuns(L, k) [15 pts]
# Write the non-destructive function shortenLongRuns(L, k) that takes a list L and a positive integer k, and 
# non-destructively returns a similar list, only without any run of k consecutive equal values in L. This means that 
# any values that would otherwise produce a consecutive run of k elements are not present. 
# For example: 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 2) == [2, 3, 5, 3]) 
# assert(shortenLongRuns([2, 3, 5, 5, 5, 3], 3) == [2, 3, 5, 5, 3]) 
# Note: your function may not just create a copy of L and call the destructive version of this function (below) on 
# that copy and return it. Instead, you must directly construct the result here.


def shortenLongRuns(n, k):
	if n == []:
		return []
	# res = []
	z = len(n)
	c = 1
	# a = n[0]
	while z > 0:
		for i in range(1, len(n)-1):
			if n[i] == n[i-1]:
				c += 1
				if c == k:
					n.remove(n[i])
					z = z - 1
			else:
		# 		res.append((c, a))
				c = 1
		# 		a = n[i]
		# res.append((c, n[-1]))
	return n

print(shortenLongRuns([2, 3, 5, 5, 5, 3], 2))


# def shortenlongruns(L, k):
# 	# Your code goes here
# 	pass