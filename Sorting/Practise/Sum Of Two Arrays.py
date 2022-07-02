
link = "https://www.codingninjas.com/codestudio/problems/sum-of-two-arrays_893186"

"""
Given two array you ahve to add them


My approach to slove this problem - 
the cases may be ---
    1. LEN(a) > len(b)
    2. Len(a) < len(b)
    3. len(a) == len(b) but there shoud be carry


    this is down by for while loop 
    1. check for both array
    2. check for first array if any index is left
    3. check for second array if any index is left
    4. check for carry
    Every one have code to fkind sum and carry



"""

def SumTwoArray(a,b):
    n = len(a)
    m = len(b)
    i = n - 1
    j = m - 1
    ans = []
    carry = 0
    while i>=0 and j >= 0:
        sum = a[i] + b[j] + carry
        carry = sum//10
        ans.append(sum%10)
        i -= 1
        j -= 1
        
     
    while i>=0:
        sum = a[i] + carry
        carry = sum//10
        ans.append(sum%10)
        i -= 1
     
    while j >= 0:
        sum = b[j] + carry
        carry = sum//10
        ans.append(sum%10)
        j -= 1
     
    while carry != 0:
        sum = carry
        carry = sum//10
        ans.append(sum%10)

    return list(reversed(ans))
          





if __name__ == "__main__":
    arr1 = [1,2,3,4]
    arr2 = [4,5,8,6]
    print(SumTwoArray(arr1,arr2))