link = "https://practice.geeksforgeeks.org/problems/add-two-numbers-represented-by-linked-lists/1"

# Problem is to add two linked list

"""
Approach-  
    add to right side
    reverse the both
    add them and take carry



"""

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None


class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first = self.reverse(first)
        second = self.reverse(second)
        carry = 0
        h = Node(0)
        l = h
        
        while first and second:
            su = first.data + second.data + carry
            carry = su//10
            n = Node(su%10)
            h.next = n
            h = h.next
            first = first.next
            second = second.next
        
        while first:
            su = first.data + carry
            carry = su//10
            n = Node(su%10)
            h.next = n
            h = h.next
            first = first.next
                
        while second:
            su = second.data + carry
            carry = su//10
            n = Node(su%10)
            h.next = n
            h = h.next
            second = second.next
        
            
        while carry != 0:
            n = Node(carry%10)
            h.next = n
            h = h.next
            carry = carry//10
        
        return self.reverse(l.next)
        
    
    def reverse(self,mid):
        prev = None
        curr = mid
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    
# both approach have same time complexity 
# in one while loop
class Solution:
    #Function to add two numbers represented by linked list.
    def addTwoLists(self, first, second):
        # code here
        # return head of sum list
        first = self.reverse(first)
        second = self.reverse(second)
        carry = 0
        h = Node(0)
        l = h
        
        while first or second or carry != 0:
            f = 0
            s = 0
            if first != None:
                f = first.data
                first = first.next
            if second != None:
                s = second.data
                second = second.next
                
            su = f + s + carry
            carry = su//10
            n = Node(su%10)
            
            h.next = n
            h = h.next
        
        
        return self.reverse(l.next)
        
    
    def reverse(self,mid):
        prev = None
        curr = mid
        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        return prev
    

