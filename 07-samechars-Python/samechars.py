# sameChars(s1, s2) [20 pts]
# Write the function sameChars(s1, s2) that takes two strings and returns True if the two strings are composed of 
# the same characters (though perhaps in different numbers and in different orders) -- that is, if every character 
# that is in the first string, is in the second, and vice versa -- and False otherwise. This test is 
# case-sensitive, so "ABC" and "abc" do not contain the same characters. The function returns False if either 
# parameter is not a string, but returns True if both strings are empty (why?).

def samechars(s1, s2):
	# Your code goes here
	if(type(s1)!=str or type(s2)!=str):
		return False
	if(len(s1)==0 and len(s2)==0):
		return True	
	f1=True
	f2=True
	for i in s1:
		if i not in s2:
			f1=False
	for i in s2:
		if i not in s1:
			f2=False
	if(f1 and f2):
		return True
	return False