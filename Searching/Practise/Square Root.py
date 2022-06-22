
link = "https://www.codingninjas.com/codestudio/problems/square-root_893351"
link = "https://leetcode.com/problems/sqrtx/"
'''
TO FIND The closest squre root we search from 0 to n and finding mid check if mid squre is greater then end = mid -1 
if less start = mid +1 else return mid 

'''


def getSqureRoot(val):

    start = 0
    end = val
    ans = 0
    while start <= end :
        mid  = (start + end)//2
        sqr  = mid*mid
        if sqr == val:
            return mid
        elif sqr > val:
            end = mid - 1
        else:
            ans = mid 
            start = mid + 1
    return ans

if __name__ == "__main__":
    print(getSqureRoot(1))