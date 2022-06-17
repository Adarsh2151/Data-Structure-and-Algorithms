'''
Given problem - An array consist of two array one is ascending and another is descending you have to find out the index through which one array is ending and another array is starting means top most element of a array at center.

Approach to solve this problem- 
    simple logic as binary search a little change that we exit when the before and after of mid is less than mid. if mid -1 is greater we understand our mid is cross the pick so end = mid. this condition vice versa


'''

def peakIndexInMountainArray(arr):

    start = 0
    end  = len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if start<mid<end and arr[mid-1]<arr[mid]>arr[mid+1]:  # check the pick
            return mid
        if arr[mid-1] > arr[mid]:
            end = mid               # don't mid -1 because the mid may be the element 
        if arr[mid-1] < arr[mid]:
            start = mid
    return -1

# Another Approach
def peakIndexInMountainArray(arr):

    start = 0
    end  = len(arr)-1

    while start <= end:
        mid = (start+end)//2
        if arr[mid] < arr[mid+1]:  # check the pick
            start = mid + 1
        else:
            end = mid
    return start







if __name__ == "__main__":
    arr = [3,4,5,1]
    print(peakIndexInMountainArray(arr))