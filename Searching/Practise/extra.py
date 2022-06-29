'''
[1,2,3,4,5,6,7,8]
[7,8,1,2,3,4,5,6]


'''

def pivotIndex(arr):
    start = 0
    end = len(arr)-1

    while start < end:
        '''
        [1,2,3,4,5,6,7,8]  Array
        [7,8,1,2,3,4,5,6]  Rotated Array
        
        in rotaded array  our pivot is 8 
        
        '''
        # in rotated array there is point throughrt 

        mid = (start + end )//2
        if arr[0] < arr[mid]:
            start = end
        else:
            end = mid - 1


    return start



if __name__ == "__main__":
    # arr = [1,7,3,6,5,6]
    arr = [2, 3, 5, 8]
    print(pivotIndex(arr))