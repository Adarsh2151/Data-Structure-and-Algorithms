link = "https://www.codingninjas.com/codestudio/problems/next-smaller-element_1112581"

# given an array you have to find out the next smaller element


""" 
We can think a approach that for every index check it next smaller by while loop. that O(n2).
which is not good we have to solve in O(n) using stack

Approach -- 
    From last we start means in stack order compare with another stack that containing minimum value default  = -1 .and after comparing add that value. It may be the next smaller of some element.
    For more detail see code- 
    


"""

def nextSmallerElement(arr,n):
    # Write your code here.
    st = [-1]
    ans = []
    for i in range(1, len(arr)+1):
        while arr[-i] <= st[-1]:
            st.pop()
        ans.append(st[-1])
        st.append(arr[-i])
    return reversed(ans)
                




