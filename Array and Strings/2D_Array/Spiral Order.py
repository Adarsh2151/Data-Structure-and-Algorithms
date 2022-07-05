
link = "https://leetcode.com/problems/spiral-matrix/"


"""
Given a 2d array you have to print of store the value in spiral series.


My Approach 1  - 
    checkout he solution and tryout 
    4 while loop in all direction and every time it  update the start end of rows and cols for spiral run 
    * Every while loop append the value to ans array
    

My Approach 2  -  
##    My own solution for context here they given a linked list to assign the value spiral

    Use less variable 
    while loop 4 times in this case first we increase a variable to go right after that we use same for go left by some logic as in approach 1
    A special thig is that if we visited index then we convert it into -1


Returns:
    list: ansArray
"""


# 1 Approach
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        ans = []
        row = len(matrix[0])
        col = len(matrix)
        
#       following variable store the index point and end point
        startRow = 0 
        endRow = row - 1
        startCol = 0
        endCol = col - 1
        
#       Count the num of  variable check if equal to total then break
        count = 0
        total = row * col
        
        while count < total:   
            
            # checking for left to right and increment startCol because we already covered start of column.
            i = startRow
            while i <= endRow and count < total:
                ans.append(matrix[startCol][i])
                i+=1
                count += 1
            startCol += 1
            
            # checking for up to down and increment endCol because we already covered every end of rows.
            i = startCol
            while i <= endCol and count < total:
                ans.append(matrix[i][endRow])
                i+=1
                count += 1
            endRow -= 1
            
            # checking for right to left and increment endCol because we already all element of end of column.
            i = endRow
            while i >= startRow and count < total:
                ans.append(matrix[endCol][i])
                i-=1
                count += 1
            endCol -= 1
            
            # checking for down to up and increment startRow because we already covered starts of Row.
            i = endCol
            while i >= startCol and count < total:
                ans.append(matrix[i][startRow])
                i-=1
                count += 1
            startRow += 1
                
    
        return ans
            
class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        
        ans = []
        n = len(matrix[0])
        m = len(matrix)
        total = m*n
        r = 0
        d = 0
        while total >0 :
            while r < n and total > 0:
                if matrix[d][r] =="-1":
                    break;
                ans.append(matrix[d][r])
                matrix[d][r] = "-1"
                total -= 1
                r +=1
            while d+1 < m and total > 0:  
                if matrix[d+1][r-1] == "-1":
                    break;      
                ans.append(matrix[d+1][r-1])
                matrix[d+1][r-1] = "-1"
                total -= 1
                d +=1
            while r-1 > 0 and total > 0:   
                if matrix[d][r-2] == "-1":
                    break;
                ans.append(matrix[d][r-2])
                matrix[d][r-2] ="-1"
                total -= 1
                r -=1
            while d > 0 and total > 0:
                if matrix[d-1][r-1] == "-1":
                    break;
                ans.append(matrix[d-1][r-1])
                matrix[d-1][r-1] = "-1"
                total -= 1
                d -=1
        return ans