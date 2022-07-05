

link = "https://leetcode.com/problems/search-a-2d-matrix/"

"""
How implement the binary search in 2d array ?
    To implement the binary search consider that it is arranged in single array. Its last index is row*col - 1 and mid will be start + end  // 2 and to get index from mid is
    arr[mid] = arr[mid//col][mid%col]


"""


""" 
Given a problem to find the element in sorted 2D array


My approach is simple to implement the above techenic 

"""


class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        """
        Our Approach is to change it into single array that is sorted
        
        
        """
        row = len(matrix)
        col = len(matrix[0])
        start = 0
        end = row*col - 1
        
        while start <= end:
            mid  = (start + end)//2
            elem = matrix[mid//col][mid%col]
            
            if target == elem:
                return True
            if target > elem:
                start = mid+ 1
            if target < elem:
                end = mid - 1
        return False