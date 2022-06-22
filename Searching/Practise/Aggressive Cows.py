"""
problem is to arrange the cows in such order where the distance between them is larger.


Our Approach -
2 function  are used -
1. A simple binary search that decide whether we have to go right or left.
2. A main function that decide whether the mid is posible answer or not 

To check mid is possible answer we write a for loop that iterate the placew of stall checking if the difference hit the upper of middle then place another cow. If count of cow == no of cow then return True. At the end return False

"""


def aggressiveCows(stall, k):
    # Write your code here.
    stall.sort()
    start = 0
    end  = max(stall) - min(stall)
    ans = -1
    while start <= end:
        mid = (start+end)//2
        if possible(mid,stall,k):
            start = mid + 1
            ans = mid
        else:
            end = mid - 1
            
    return ans      
            
def possible(mid,stall,k):
    cowCount = 1
    lastPos = stall[0]
    for i in stall:
        if i - lastPos >= mid:
            cowCount += 1
            if cowCount == k:
                return True
            lastPos = i
    return False
    

if __name__ == "__main__":
    stall = [4,2,1,3,6]
    k  = 2
    print(aggressiveCows(stall,k))