link = "https://leetcode.com/problems/string-compression/"
"""
Given a problem to add occurance of character in same array if came with two or more digit then split it and add 


"""

class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        """
        
        """
        My approach to solve this problem -- 
        
        Inside while loop
        1. check how successive values are 
        2. add character in ansIndex and increment it to add count
        3. if count is grater than 1 the change to stroing and add it.
        
        
        
        """
        
        
        i = 0
        ansIndex = 0
        n = len(chars)
        
        while i<n:
            
            j = i
            while j < n and chars[i] == chars[j] : # while cheaking next value equal means counting occurance
                j += 1
                
            chars[ansIndex]  = chars[i] # adding the checked character 
            ansIndex += 1 # increamenting for count 
            count = j - i
            
            if count > 1:
                # if len of digit is grater than 10 so split 
                for char in str(count):
                    chars[ansIndex] = char
                    ansIndex += 1
            
            i = j
                    
        return ansIndex
            
            
        
        
        