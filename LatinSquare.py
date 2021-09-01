# isLatinSquare(a)
# Write the function isLatinSquare(a) that takes a 2d list 
# and returns True if it is a Latin square and False otherwise.

# Check for Latin square in the following link:
# https://en.wikipedia.org/wiki/Latin_square

# Write your own test cases...

def isLatinSquare(lst):
    # Your code goes here...
    
    if(len(lst)!=len(lst[0])):
        return False
    for i in range(len(lst)):
        r=lst[i]
        if(len(set(r))!=len(r)):
            return False
        r=[]
    c=[]
    for i in range(len(lst[0])):
        for j in range(len(lst)):
            c.append(lst[j][i])
        if(len(set(c))!=len(c)):
            return False
        c=[]
    return True


lst=[['1','2','3'],['2','3','1'],['3','1','2']]
lst2=[['1','2','3'],['2','3','1'],['3','1','1']]
lst3=[['1','2','3'],['2','2','1'],['3','2','2']]

assert(isLatinSquare(lst)==True)
assert(isLatinSquare(lst2)==False)
assert(isLatinSquare(lst3)==False)
print("Pass")
