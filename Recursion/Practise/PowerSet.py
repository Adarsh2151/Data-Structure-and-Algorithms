# Power Set 
link = "https://leetcode.com/problems/subsets/"
"""
power set is set of all subset-
The number of subset of any set be 2^n 


My Approach to solve it 
    take or not take recursively
    


"""
va = []

def PowerSet(s,sub = [],index = 0):
    # if sub not in va:
    
    if index >= len(s):
        va.append(sub)
        return sub
    PowerSet(s,sub,index+1)
    PowerSet(s,sub+[s[index]],index+1)
    return va



if __name__ == "__main__":
    arr = [1,2,3]
    ps = PowerSet(arr)
    print(va,ps)