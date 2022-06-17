# By the help of recursion
def binarySearchR(arr,start,end,key):
    if start > end:
        return "Not Found"
    mid = (start+end)//2
    if arr[mid] == key:
        return mid
    elif key > arr[mid]:
        start = mid+1
        return binarySearch(arr,start,end,key)
    elif key < arr[mid]:
        end = mid-1
        return binarySearch(arr,start,end,key)

# By the help of loop
def binarySearch(arr,start,end,key):
    while start <= end:
        mid = (start+end)//2
        if arr[mid] == key:
            return mid
        elif key > arr[mid]:
            start = mid+1
        elif key < arr[mid]:
            end = mid-1
    return "Not Found"











if __name__ == "__main__":
    # arr = [1,2,5,8,6,8,2,4,5,6,9,3,7]
    arr = [1,3,4,6,7,8,9]
    key = 9
    print(binarySearch(arr,0,6,key))