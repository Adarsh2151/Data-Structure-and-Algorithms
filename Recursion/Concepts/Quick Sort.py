
"""
Quick sort is a sorting algorithm that works as -- 
    Recurise from pivot point
    partiton
    
    The theory - take one element and put it to right place the perform some logical operation by which left to the pivot should be less than pivot and right to pivot should be greater than pivot. 
    
    after partition send the left and right to quick sort
    



"""



def QuickSort(arr,start,end):
    # Base case
    if start >= end:
        return 
    
    p,arr = partion(arr,start,end) # finding pivot index and sorting the left and right part by partion function
    
    QuickSort(arr,start,p) # Left Part
    QuickSort(arr,p+1,end) # Right Part
    
    return arr


def partion(arr,s,e):
    k = arr[s]
    p = s
    for i in range(s,e): # count the occurance of lesser element than k
        if arr[i] < k:
            p += 1
            
    arr[s],arr[p] = arr[p],arr[s]  # swapping pivot to its position 
    
    while s<e: # function arrangeb the arr 
        if arr[s] >= k and arr[e-1] < k:
            arr[s],arr[e-1] = arr[e-1],arr[s]
            s += 1
            e -= 1
        elif arr[s] < k and arr[e-1] < k:
            s+= 1
        elif arr[s] > k and arr[e-1] > k:
            e-= 1
        else:
            s+= 1
            e -= 1
            
    return p,arr
    
    
    

if __name__ == "__main__":
    arr = [5,4,6,3,8,1,2,7]
    # arr = [9, 9, 9, 8, 2, 3, -6]
    arr = [5,3,6,2,1,4]
    print(QuickSort(arr,0,len(arr)))