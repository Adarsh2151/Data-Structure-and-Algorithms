"""
Adaptable  Stable Algorithm 

Approach - first for loop that iterate then check while left is less and swap again and again
            After that assign value of arr[j] = key

Insertion Sort - 
    - Iterate all index and check for every index element while less than left SHIFT that
        eg -   [7,9,6,2,4]
               [7,9,6,2,4]
               [7,6,9,2,4]
               [6,7,9,2,4]
               [6,7,2,9,4]
               [6,2,7,9,4]
               [2,6,7,9,4]
               [2,6,7,4,9]
               [2,6,4,7,9]
               [2,4,6,7,9] # FOUND Sorted
      Use Case - Adaptable and stable
    - Time Complexity - O(n2) Space Complexity - O(1)
    - Best Case O(n) worst case complexity O(n2)

"""
def InsertionSort(arr):
    n = len(arr)
    for i in range(n):
        k = arr[i] # created for storing ith value
        j = i
        while 0<j<n and arr[j]<arr[j-1]: # comparing with left 
            arr[j],arr[j-1] = arr[j-1],arr[j]
            j -= 1
        arr[j] = k
    return arr


if __name__ == "__main__":
    arr = [4,9,6,3,8,5,10,7]
    print(InsertionSort(arr))