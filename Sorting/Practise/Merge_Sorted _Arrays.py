"""
Given a problem to merge the two sorted list there is the length of first sorted list consist of m +n length where m is len of list1 and n is another . You have to sort in list1

My appraoch to solve this problem -  first try to merge in the len m in which item alraedy asign. for this I check if nums [j] < nums[i] then swap these and sort the nums2.

To add in 0 part - with the linear iteration append the rest sorted value



""" 
 
 
  #         my approach to solve it -- 
        
#         here both are sorted then we go to nums1 iteratively. j will be another variable that check in nums2
         
def merge( nums1, m, nums2, n):
    i = 0
    j = 0
    while j<n and i < m: 
        if nums1[i] > nums2[j]:
            nums1[i], nums2[j] = nums2[j], nums1[i]
        nums2.sort() # to handle some case
        i += 1
    while j < n:
        nums1[i] = nums2[j]
        j += 1
        i += 1
    return nums1




if __name__ == "__main__":
    arr1 = [1,2,3,0,0,0]
    arr2 = [2,5,6]
    m = 3
    n = 3
    print(merge(arr1,m,arr2,n))