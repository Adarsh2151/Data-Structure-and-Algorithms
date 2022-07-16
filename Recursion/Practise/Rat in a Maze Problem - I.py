
link = "https://practice.geeksforgeeks.org/problems/rat-in-a-maze-problem/1"
"""

Given a problem you have to go the last coordinate from first. you can go only through 1 not 0. find the steps taken to reach


My approach to solve this problem - 
1. check that first coordinate is not zero
2. use solve function to get answer
3. check that in which direction we go("LRUD") where visited matrix index will be 0 and matrix index will be 1
4. in order to recursively calling after that backtrack it and store the what step is taken
5.if base case means row== col == n-1 then return.

"""
ans = []
visited = [[0 for i in range(4)] for _ in range(4)]
def rat(matrix,row = 0,col = 0,step = ""):
    if [len(matrix)-1,len(matrix)-1] == [row,col]:
        ans.append(step)
        visited[row][col] = 0
        return
    if checkHor(matrix,row,col+1):

        step += "R"
        rat(matrix,row,col+1,step)
        step = step[:-1]
    
    if checkVer(matrix,row+1,col):
        step += "D"
        rat(matrix,row+1,col,step)
        step = step[:-1]
    
    if checkHor(matrix,row,col-1):
        step += "L"
        rat(matrix,row,col-1,step)
        step = step[:-1]
    
    if checkVer(matrix,row-1,col):
        step += "U"
        rat(matrix,row-1,col,step)
        step = step[:-1]

    visited[row][col] = 0
def checkHor(matrix,row,col):
    if 0<=col < len(matrix) and visited[row][col]==0 and matrix[row][col]==1:
        visited[row][col] = 1
        return True
def checkVer(matrix,row,col):
    if 0<=row < len(matrix) and visited[row][col]==0 and matrix[row][col]==1:
        visited[row][col] = 1
        return True

    return False

if __name__ == "__main__":
    mat = [[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]]
    print(rat(mat))
    print(ans)
    
    
    
    
    
    
    
    
#     User function Template for python3
# #User function Template for python3

class Solution:
    def findPath(self, m, n):
        # code here
        self.ans = []
        if m[0][0] == 0:
            return self.ans
            
        self.visited = [[0 for i in range(n)] for _ in range(n)]
        
        self.solve(m,n,self.visited)
        self.ans.sort()
        return self.ans
        
    def solve(self,m,n,visited,row = 0,col = 0,st = ""):
        if row == col == n-1:
            self.ans.append(st)
            return
        self.visited[row][col] = 1
        if self.check(m,row+1,col,n):
            st += "D"
            self.solve(m,n,visited,row+1,col,st)
            st = st[:-1]
            
        if self.check(m,row,col-1,n):
            st += "L"
            self.solve(m,n,visited,row,col-1,st)
            st = st[:-1]
            
        if self.check(m,row,col+1,n):
            st += "R"
            self.solve(m,n,visited,row,col+1,st)
            st = st[:-1]
            
        if self.check(m,row-1,col,n):
            st += "U"
            self.solve(m,n,visited,row-1,col,st)
            st = st[:-1]
            
        self.visited[row][col] = 0
    def check(self,m,row,col,n):
        if 0 <= row< n and 0<= col < n and m[row][col] == 1 and self.visited[row][col] == 0:
            return True
        return False
        
s = Solution()
print(s.findPath([[1,0,0,0],[1,1,0,1],[1,1,0,0],[0,1,1,1]],4))
print(s.findPath([[1,1],[1,1]],2))

