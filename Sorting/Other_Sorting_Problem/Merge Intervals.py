link = "https://leetcode.com/problems/merge-intervals/"

def merge(intervals):
    
    """
    My approach to solve this problem 
    
    first of all sort the array to get successive value to find
    loop from start to end - 1 and check that start th last is part of start +1 th means >= . then change start + 1 [0] to both min and [1] to both max.
    
    In the else condition add the that value to new list
    
    """
    intervals.sort()
    
    start = 0
    end = len(intervals)
    combining_index = []

    while start < end-1:
        if intervals[start][1] >= intervals[start+1][0]  :
            intervals[start+1][0] = min(intervals[start][0],intervals[start+1][0])
            intervals[start+1][1] = max(intervals[start][1],intervals[start+1][1])
        else:
            combining_index.append(intervals[start])
        start += 1
    combining_index.append(intervals[-1])
    return combining_index

if __name__ == "__main__":
    arr = [[1,4],[4,6]]
    print(merge(arr))