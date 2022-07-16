link = "https://www.codingninjas.com/codestudio/problems/subsequences-of-string_985087"

"""
same as power set 

some difference is don't need "".
eg - abc -- a,b,c,ab,ac,bc,abc

"""


def subsequences(str):
    # Write your code here
    va = []
# se = set()

    def PowerSet(s,sub = "",index = 0,val = []):
        # if sub not in va:
        if index >= len(s):
            if len(sub)> 0:
                va.append(sub)
            return sub
        PowerSet(s,sub,index+1,val )
        PowerSet(s,sub+s[index],index+1,val)
        return val
    PowerSet(str)
    return va



if __name__ == "__main__":
    print(subsequences("abc"))