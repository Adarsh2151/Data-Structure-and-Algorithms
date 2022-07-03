
link = "https://leetcode.com/problems/permutation-in-string/"
"""
    Given an problem that you have to find out wheater any permutation of s1 present in s2 ?
    
    
    Try to solve in O(s1+s2)
"""
class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        My Approach - 
        
        s1 - store character count
        s2 - Traverse with a windows(small sub of len s1 eg.. ab, eo ) of s1 length 
        if not found then use while loop in len of s2 and create there window and check is equal
             
        """
        # The following line of code just count the character of s1 string
        s1_count = [0 for _ in range(26)]
        for i in s1:
            asci = ord(i) -ord("a")
            s1_count[asci] += 1
        
        # Traverse in s2 with window size means taking the len of s1 
        s2_count = [0 for _ in range(26)]
        s1_size = len(s1)
        index = 0
        while len(s2)> index < s1_size:
            asci = ord(s2[index])-ord("a")
            s2_count[asci] += 1
            index += 1
        if s1_count==s2_count:
            return True
        
        # checking for next possible window 
        while index < len(s2):
            # Adding new character lenght
            asci = ord(s2[index])-ord("a")
            s2_count[asci] += 1
            
            # Removing old character length
            asci = ord(s2[index-s1_size])-ord("a")
            s2_count[asci] -= 1
            
            index += 1
            if s1_count == s2_count:
                return True