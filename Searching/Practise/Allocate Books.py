link = "https://www.codingninjas.com/codestudio/problems/allocate-books_1090540"


#  Book Allocation

"""     problem -
1. Each student gets at least one book.
2. Each book should be allocated to a student.
3. Book allocation should be in a contiguous manner.
Given a list of books i have to distribute these book sucyh a way that the list of maximum of every allocation will minimum


# My Approach - To implement the binary search in the problem we take start 0 and will be highest their sum . while loop till start <= end:
every time calculte mid check that this mid will  be our answer. to check mid add evry element of arr and if the sum will greater than mid then count += 1 that alloted to other because maximum is mid.if all set return True.

If True then we understand that the greater than the mid is algpo answer so we go to left.


"""

def allocateBooks(arr, n, m):
    ans = 0
    start = 0
    end = sum(arr)
    while start <= end:
        mid  =  (start+end)//2
        val = checkMid(mid,m,arr)
        if val:
            ans = mid
            end = mid -1 
        else:
            start = mid + 1
    return ans


def checkMid(mid,m,arr):
    val = 0
    count = 1
    index = 0
    while index < len(arr):
        val += arr[index]
        if val > mid:
            count += 1
            val = arr[index]
            if count > m or arr[index] > mid:
                return False

        index += 1
    return True
        
        
        



if __name__ == "__main__":
    arr = [5,17,100,11]
    m = 4
    n = 4
    print(allocateBooks(arr,n,m))