# removeDuplicate(text) [10 pts]
# Write a program to remove all the duplicate characters from a given input String,e.g.
# if given String is "JavaPython" then the output should be "JavPython".
# The second or further occurrence of duplicate should be removed.

def removeduplicate(text):
	a = []
	for i in text:
		if i not in a:
			a.append(i)
	# b = set(a)
	c = ""
	for j in a:
		c += j
	return c

	