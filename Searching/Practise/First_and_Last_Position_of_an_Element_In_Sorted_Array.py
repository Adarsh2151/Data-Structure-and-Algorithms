"https://www.codingninjas.com/codestudio/problems/first-and-last-position-of-an-element-in-sorted-array_1082549"


def firstAndLastPosition(arr, n, k):
    """
        My approach to solve this problem-
            solve in two parts find first and last separatly by O(2logn)
            if mid matches then set end = mid - 1 to check the leftmost index and do start = mid +1 to get rightmost index.

    
    """
    start = 0
    end = n - 1
    first = -1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == k:   #  we donnot return mid but store in variable that check to the end as mid
            first = mid
            end = mid - 1       
        elif k < arr[mid]:
            end = mid - 1
        
        else:
            start = mid + 1

    start = 0
    end = n - 1
    last = -1
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == k:
            last = mid
            start = start + 1
        elif k < arr[mid]:
            end = mid - 1
        
        else:
            start = mid + 1

    return first,last
        




if __name__ == "__main__":
    arr = [1,1,2,2,2,4,5,5,7,8,9]
    print(firstAndLastPosition(arr,len(arr),2))
