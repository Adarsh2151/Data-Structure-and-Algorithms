link = 'https://leetcode.com/problems/check-if-array-is-sorted-and-rotated/'
"""
Given a rotated array you have to find whethear it is sorted or not 


My Approach to solve it 
- Find how many pivot index are there. By using a logic 'if nums[i-1] > nums[i]' means that if successor is less then count it.



"""

def check( nums):
    count = sum(1 for i in range(len(nums)) if nums[i-1] > nums[i])
    if count <= 1:
        return True

if __name__ == "__main__":
    arr = [5,6,7,4,3,2]
    print()