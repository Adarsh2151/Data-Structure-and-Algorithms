link = "https://www.codingninjas.com/codestudio/problems/search-in-rotated-sorted-array_1082554"
'''
Search in rotated sorted array
    A array is first sorted then we rotated it from a point known as pivot index

    you have find the given key in this array 
    Approaches to solve this problem
    -- first find out pivot point 
    if first index of array is less than key then search only to pivot poin else search from pivot point
    Use Binary search

'''
def getPivot(arr):
    start = 0
    end = len(arr) - 1
    while start < end :
        mid  = (end+start)//2
        if arr[0] <= arr[mid]:
            start = mid + 1
        else:
            end = mid 

    return start


def findPosition(arr, k):

    pi = getPivot(arr)

    # go from first to pivot point
    if k >=arr[0]:
        start = 0
        end = pi

    
    #  Go from the pivot point to last
    else:
        start = pi
        end = len(arr)-1
    

    #  Simple Binary  Search Algorithm
    while start <= end:
        mid  = (start+end)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == "__main__":
    arr = [8, 10, 12, 15, 2]
    print(findPosition(arr,2))