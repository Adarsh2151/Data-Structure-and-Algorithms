
link = "https://leetcode.com/problems/permutations/"
""" 
Given an problem to find all permutation of array

My approach - trying to put all element at all position
    Approach1 - Datastructure and space complexity
    Approach2 - fixing all to all position
    
    Approach1 - 
    first array is given to find all you have to swap all to index and so on, means that every at every position

    


"""
                   
from typing import List


ans = []
    
def helper(nums,ans,index = 0):
   
    if len(nums) == index:
        ans.append(nums)
    for i in range(index,len(nums)):
        nums[index],nums[i] = nums[i],nums[index]
        helper(list(nums),ans,index+1)  # without use of list get same array duplicated in all
    return ans
print(helper([1,2,3],ans))
