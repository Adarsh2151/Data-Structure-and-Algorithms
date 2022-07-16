

#  find array sum problem by recursion
def findArraySum(arr,index = 0):
    if len(arr) == 0:return 0
    if len(arr) <= index+1:
        return arr[index]
    return arr[index] + findArraySum(arr,index+1)


# Linear search
def LinearSearch(arr,target,index = 0):
    if len(arr) <= index:
        return False
    if arr[index] == target:
        return True
    return LinearSearch(arr,target,index+1)


# Binary Search
def BinarySearch(arr,start,end,target):
    if start > end:
        return False
    mid = (start+end)//2
    if arr[mid] == target:
        return True
    elif arr[mid] > target:
        return BinarySearch(arr,start,mid-1,target)
    else:
        return BinarySearch(arr,mid+1,end,target)


if __name__ == "__main__":
    # arr = [1,1,1,1,1,8,1,11,1,]
    # print(findArraySum(arr))

    # arr = [4,5,86,64,3,8,2,9,4,6,145,7]
    # print(LinearSearch(arr,45))

    arr = [4,5,86,64,3,8,2,9,4,6,145,7]
    print(BinarySearch(arr,0,len(arr)-1,4))
    

    print(sum(arr))