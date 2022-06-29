"""
1. Selection Sort -

Selection Sort - 
    - insert the ith minimum value at ith position by swapping
    first take the 0 th index then check the minimum in rest if found then swap further go to n - 1 index
    - Time complexity is O(n2) same in best case and worst case

    Use Case - If size of arr is small
    
    Create FlowChart of this algorithm

"""
def selection_sort(arr):

    for i in range(len(arr)-1):
        for j in range(i,len(arr)):
            if arr[j] < arr[i]:
                arr[j],arr[i] = arr[i],arr[j]

    return arr


if __name__ == "__main__":
    arr = [8,6,9,3,74,9,3,]
    print(selection_sort(arr))