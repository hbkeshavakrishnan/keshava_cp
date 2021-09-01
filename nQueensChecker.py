# nQueensChecker(a)
# Background: The "N Queens" problem asks if we can place N queens on an NxN chessboard such that no two queens are attacking each other. For most values of N, there are many ways to solve this problem. Here, you will write the function nQueensChecker(board) that takes a 2d list of booleans where True indicates a queen is present and False indicates a blank cell, and returns True if this NxN board contains N queens all of which do not attack any others, and False otherwise.

def nQueensChecker(a):
    # Your code goes here...
    l=[]
    for i in range(len(a)):
        for j in range(len(a[0])):
            if(a[i][j]==True):
                l.append((i,j))
    for i in range(len(l)-1):
        for j in range((i+1),len(l)):
            qR=l[i][0]
            qC=l[i][1]
            oR=l[j][0]
            oC=l[j][1]
            if canqueenattack(qR, qC, oR, oC)==True:
                return False
    return True
    
def canqueenattack(qR, qC, oR, oC):
	# Your code goes here
	if(qR==oR or qC==oC or abs(qR-oR)==abs(qC-oC)):
		return True
	return False


board1=[[False,True,False,False],[False,False,False,True],[True,False,False,False],[False,False,True,False]]
board2=[[False,True,True,False],[False,False,False,True],[True,False,False,False],[False,False,True,False]]
assert(nQueensChecker(board1)==True)
assert(nQueensChecker(board2)==False)
print("Testcases Passed")