# leastFrequentLetters(s) [20 pts]
# Write the function leastFrequentLetters(s), that takes a string s, and ignoring case (so "A" and "a" are treated 
# the same), returns a lowercase string containing the least-frequent alphabetic letters that occur in s, each 
# included only once in the result and then in alphabetic order. So:
# leastFrequentLetters("aDq efQ? FB'daf!!!") 
# returns "be". Note that digits, punctuation, and whitespace are not letters! Also note that seeing as we have not 
# yet covered lists, sets, maps, or efficiency, you are not expected to write the most efficient solution. Finally, 
# if s does not contain any alphabetic characters, the result should be the empty string ("")

def charcount(s, k):
	c=0
	for i in s:
		if(i==k):
			c=c+1
	return(c)
# print(charcount("harsha", "a"))

def leastfrequentletters(s):
	s=s.lower()
	# print(s)
	c=len(s)
	temp=""
	for i in s:
		if(i.isalpha()):
			x=charcount(s, i)
			if(x<c):
				c=x
				temp=i
			elif(x==c):
				temp+=i
	
	return(''.join(sorted(temp)))