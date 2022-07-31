# check palindrome .eg racecar

link = "https://practice.geeksforgeeks.org/problems/check-if-linked-list-is-pallindrome"
""" 
Approach1 - 
    - put all data to array 
    - check pallindrome
    
Approach - 
    find middle
    reverse after mid
    compare them
    reverse it to get normal
    
    

"""


class Solution:
    def isPalindrome(self, head):
        if head.next == None:
            return True

        #code here
        mid = self.getMid(head)
        
        
        # revere the 
        mid.next = self.reverse(mid.next)
        
        # compare
        head2 = mid.next
        while head2:
            if head.data != head2.data:
                return False
            head = head.next
            head2 = head2.next
        return True
        
    def reverse(self,mid):
        prev = None
        curr = mid
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    def getMid(self,head):
        h = head.next
        
        while  h != None and h.next != None :
            head = head.next
            h = h.next.next
        return head
