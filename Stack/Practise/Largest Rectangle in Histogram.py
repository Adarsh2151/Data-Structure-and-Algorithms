
link = "https://leetcode.com/problems/largest-rectangle-in-histogram/"

"""
Given a heigths of histogram a bar ca extend where as len of bar is greater than or equal.
your task is to find the maximum area formed by height and width 

Approach -- 
    We have given a height so we need to find the width or expansion may be 
    - Check the next smaller from where it can be extend
    - Check the prev smaller from whre if can be extend 
    Note : Remember that we have to store or work with indexes to find distance

"""
class Solution:   # O(n)
#   main function 
    def largestRectangleArea(self, heights) -> int:
        a  = self.nextSmallerElement(heights)   # check the right expansion
        b = self.prevSmallerElement(heights)    # check the left expansion
        
        # add both value to get width and multiply by height
        area = 0
        for i in range(len(heights)):
            area = max(area,heights[i]*(a[-(i+1)]+b[i]))

        return area
    
    
    
    def nextSmallerElement(self,arr):
        # Write your code here. 
#         -1 -1 2 2 -1 1
        st = [-1]
        ans = []
        for i in range(len(arr)-1,-1,-1):
            while st[-1] != -1 and arr[i] <= arr[st[-1]]: # checking next smaller elemnt
                st.pop()
                
            g = st[-1]-i  
            if  st[-1] == -1 :  # if next not found the we thinkl that that is smaller so it goes to last
                g = len(arr)-i

            ans.append(g)
            st.append(i)
                
        return ans

    
    def prevSmallerElement(self,arr):
        # Write your code here. 
#         -1 -1 2 2 -1 1
        st = [-1]
        ans = []
        for i in range(len(arr)): # start from 0
            
            while st[-1] != -1 and arr[i] <= arr[st[-1]]:
    
                st.pop()
            g = i-st[-1]-1
            if  st[-1] == -1 : #previously not found any smaller so index will be width
                g = i
            ans.append(g)
            st.append(i)
                
        return ans


        
        