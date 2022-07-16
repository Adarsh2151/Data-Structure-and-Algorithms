
link = "https://leetcode.com/problems/letter-combinations-of-a-phone-number/"

""" 
Given a problem that in button phone. what may be the possible string typed when press these button.
eg - "23" {'ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf'}


My approach - 
 It can be solve recursively there is fixed that no. of character of string formed is always same.So this is base case.
 
 
 for loop helps to get all the possible character by pushing any button
 
 
 
"""



ans = []  # global avriable to store answer
def letter(di,digits,index = 0,opt = ""):
    # Base Case
    if index >= len(digits):
        if opt != "":
            ans.append(opt)
        return
    # string related to keypad
    s = di[digits[index]]
    # iterate string s and call function recursively
    # we use here backtracking to go through all value
    for i in s:
        opt+=(i)
        letter(di,digits,index +1,opt)
        opt = opt[:-1]
        
if __name__ == "__main__":
    di = {"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
    digits = "23"
    print(letter(di,digits))
    print(ans)


