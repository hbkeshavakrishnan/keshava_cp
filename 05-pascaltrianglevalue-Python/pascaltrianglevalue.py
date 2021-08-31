# Write the function pascalsTriangleValue(row, col) 
# that takes int values row and col, and returns the 
# value in the given row and column of Pascal's 
# Triangle where the triangle starts at row 0, and 
# each row starts at column 0. If either row or col 
# are not legal values, return None, instead of crashing. 




def fun_pascaltrianglevalue(row, col):
	numRows=row+1
	if(col>row):
		return 0
	if(row==0):
		return 1
	tri=[[1]]
	for i in range(1,numRows):
		row1=[1]
		for j in range(1,i):
			row1.append(tri[i-1][j-1]+tri[i-1][j])
		row1.append(1)
		tri.append(row1)
	return(tri[-1][col])