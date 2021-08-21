# Write the function lookAndSay(a) that takes a list of numbers and returns a list of numbers
# that results from "reading off" the initial list using the look-and-say method, using tuples 
# for each (count, value) pair.
# 
# For example:
# lookAndSay([]) == []
# lookAndSay([1,1,1]) == [(3,1)]
# lookAndSay([-1,2,7]) == [(1,-1),(1,2),(1,7)]
# lookAndSay([3,3,8,-10,-10,-10]) == [(2,3),(1,8),(3,-10)]
# lookAndSay([3,3,8,3,3,3,3]) == [(2,3),(1,8),(4,3)]

# def lookandsay(a):
# 	res = []
# 	for i in a:
# 		if i not in res:
# 			b = a.count(i)
# 			res.append((b,i))
# 		else:
# 			continue
# 	return res


def lookandsay(n):
	if n == []:
		return []
	res = []
	c = 1
	a = n[0]
	for i in range(1, len(n)):
		if n[i] == a:
			c += 1
		else:
			res.append((c, a))
			c = 1
			a = n[i]
	res.append((c, n[-1]))
	return res


print(lookandsay([-1,2,7]))













