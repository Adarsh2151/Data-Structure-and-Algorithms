
link = "https://leetcode.com/problems/search-a-2d-matrix-ii/"


"""
Given a problem where row and col both are sorted that means you entire element are not sorted you have to find the element by binary search



My Approach to solve this problem - First it is clear that if we found a number that is greater than target , we conclude there may not in down to column if smaller than not left to the row.
So we start from row 0 col end means top-right 
if elem == target: return
if elem <target : row  ++
else: col --


"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        row = len(matrix)
        col = len(matrix[0])
        
        rowIndex = 0
        colIndex = col - 1
        while rowIndex < row  and colIndex >= 0:
            elem = matrix[rowIndex][colIndex]
            if elem == target:
                return True
            if elem < target:
                rowIndex += 1
            else:
                colIndex -= 1