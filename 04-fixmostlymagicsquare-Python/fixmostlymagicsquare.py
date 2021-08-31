# fixMostlyMagicSquare(L) [15 pts]
# In this week's writing session, we wrote isMostlyMagicSquare(L). Here, say we have a mostly magic square L, but 
# then we modify L by changing exactly one value in L so that it no longer is a mostly magic square. For this 
# exercise, we assume we have just such a list L, and your task is to find and fix that change. So, given the list 
# L, return a new list M such that M is the same as L, only with exactly one value changed, and M is a mostly magic 
# square.


def fixmostlymagicsquare(L):
	# Your code goes here
	rsl=[]
	csl=[]
	for i in range(len(L)):
		rsl.append(sum(L[i]))

	cs=0
	for i in range(len(L[0])):
		for j in range(len(L)):
			cs+=L[j][i]
		csl.append(cs)
		cs=0
	
	r=probrow(rsl)
	c=probcol(csl)
	v=valchange(csl)
	L[r][c]-=v

	return L

def getCount(a,v):
	c=0
	for i in range(len(a)):
		if(a[i]==v):
			c+=1
	return c
	
def probrow(a):
	for i in range(len(a)):
		x=getCount(a,a[i])
		if(x==1):
			return i

def valchange(a):
	ma=max(a)
	mi=min(a)
	if(getCount(a,ma)==1):
		return (ma-mi)
	if(getCount(a,mi)==1):
		return (mi-ma)

def probcol(a):
	for i in range(len(a)):
		x=getCount(a,a[i])
		if(x==1):
			return i