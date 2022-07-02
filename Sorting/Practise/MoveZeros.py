link  = "https://leetcode.com/problems/move-zeroes/"
"""
Give an array you have to move all its zeros to the end


My approach to solve this problem - first take a variable j that tells on which position we append non zero value 

"""
def moveZero(nums):
    j = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i],nums[j] = nums[j],nums[i]
            j += 1
    return nums

if __name__ == "__main__":
    nums = [1,0,1,2,0,0,3,4,5,0]
    print(moveZero(nums))
        