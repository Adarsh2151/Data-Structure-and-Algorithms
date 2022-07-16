

def reverseRecursion(s,start,end):
    if start >= end:
        return s
    s = s[:start]+s[end]+s[start+1:end]+s[start]+s[end+1:]

    return reverseRecursion(s,start+1,end-1)


def checkPalindrome(s, start = 0):
    end  = len(s)-start-1
    if start > end :
        return "It is palindrome"
    if s[start] != s[end]:
        return "It is not palindrome"
    return checkPalindrome(s,start+1)


def power(a,b):
    if b == 1:
        return 2
    if b == 0:
        return 1
    sub = power(a,b//2)
    remain = 2
    if b%2==0:
        remain = 1
    return remain*sub*sub
    

# buble sort                                   

def BubbleSort(arr,end):
    if end < 1:
        return arr
    for i in  range(end-1):
        if arr[i] > arr[i+1]:
            arr[i+1],arr[i] = arr[i],arr[i+1]
    return BubbleSort(arr,end-1)


if __name__ == "__main__":
    s = "racecar"
    print(reverseRecursion(s,0,len(s)-1))
    print(checkPalindrome(s))
    print(power(2,9),2**9)
    arr = [5,86,9,4,9,3,7,1,2,9,3,78,5]
    print(BubbleSort(arr,len(arr)))