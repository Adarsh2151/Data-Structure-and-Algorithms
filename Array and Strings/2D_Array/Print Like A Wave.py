link ="https://www.codingninjas.com/codestudio/problems/print-like-a-wave_893268"


"""

Given a problem to print in wave means go down and down to up 


My simple approach 



"""

def wavePrint(arr, nRows, mCols):
    
    # Write your code here.
    # Return a list of integers denoting the sine wave of the matrix
    ans  = []
    row = 0
    col = 0
    i = 0
    increase = 1
    while i < nRows*mCols:
        if row >= nRows:
            row -= 1
            col += 1
            increase = -1
        if row < 0:
            row += 1
            col += 1
            increase = 1
        ans.append(arr[row][col])
        i += 1
        row += increase
    return ans