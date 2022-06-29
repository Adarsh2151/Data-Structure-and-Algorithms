"""
Bubble Sort - 
    - compare with neighbour element if A[i+1] < A[i] then swap it. this will get the first largest element at there position.
        Perform this for n-1 times that will arrange all the largest value from last to first
    - eg:       [4, 9, 6, 3, 8, 5, 10, 7]
                [4, 6, 3, 8, 5, 9, 7, 10]
                [4, 3, 6, 5, 8, 7, 9, 10]
                [3, 4, 5, 6, 7, 8, 9, 10]
                [3, 4, 5, 6, 7, 8, 9, 10]
                [3, 4, 5, 6, 7, 8, 9, 10]
                [3, 4, 5, 6, 7, 8, 9, 10]
                [3, 4, 5, 6, 7, 8, 9, 10]
    Use Case - In ith iteration we put ith largest element to its position
    - Time complexity - O(n2) , Space complexity = O(1)
    - Best Case - O(n) 
    * In place sorting - Do not use extra space




"""

def BubbleSort(arr):
    for i in range(1,len(arr)):
        sorted = True # this will determine that wheater we swapped or not if not then arr is sorted
        for j in range(len(arr)-i): # because last i index is sorted
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                sorted = False
        if sorted:
            break
    return arr

if __name__ == "__main__":
    arr = [4,9,6,3,8,5,10,7]
    print(BubbleSort(arr))