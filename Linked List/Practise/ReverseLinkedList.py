from typing import Iterable


link = "https://www.codingninjas.com/codestudio/problems/reverse-the-singly-linked-list_799897"


"""
 Two approach 
    1. Recursion
    2. Iterable
"""

class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None
        
        
class LinkedList:
    
    def __init__(self,val) -> None:
        self.head = Node(val)
        self.temp = self.head
        
    
    def append(self,val):
        n = Node(val)
        self.temp.next = n
        self.temp = self.temp.next
    def insert(self,pos,val):
        j = Node(val)
        h = self.head
        
        if pos == 0:
            j.next = h
            self.head = j
            return
        
        i = 1
        while h is not None:
            if i == pos:
                te = h.next
                h.next = j
                j.next = te
                return
            i += 1

    def deleteNode(self,pos):
        if pos == 1:
            self.head = self.head.next

        i = 2
        prev = self.head
        curr =  self.head.next
        while curr:
            if pos==i:
                prev.next = curr.next
            i+=1
            prev = prev.next
            curr = curr.next
    
    def print(self):
        aa = []
        a = self.head
        while a != None:
            aa.append(a.data)
            a = a.next 
        print(aa)
        
        
        
# Approach to solve this problem
#     Iteratevely link current node to previous node and go to next node by storing previous node.



def reverse(ll):
    prev = None
    h = ll.head
    while h:
        forward = h.next
        h.next = prev
        prev = h
        h = forward
    ll.head = prev
    return ll
        
 
        
def reverseLinkedList(head):
    # Base Case 
    if head == None or head.next == None:
        return head
    
    restReverse = reverseLinkedList(head.next)
    
    head.next.next = head
    head.next = None
    
    
        


if __name__ == "__main__":
    l1 = LinkedList(0)
    l1.append(1)
    l1.append(-1)
    # l1.append(3)
    # l1.append(4)
    # l1.append(5)
    # l1.append(6)
    # l1.append(7)
    l1.print()
    r = reverse(l1.head)

    r.print()
    