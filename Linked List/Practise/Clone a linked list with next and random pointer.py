
link = "https://practice.geeksforgeeks.org/problems/clone-a-linked-list-with-next-and-random-pointer"
""" 
In this problem there is change in structure of node where another pointer is storing any random node 

Node:
    data
    next
    random


"""

""" 
Approach to solve:
    Approach1 - O(n2)
    
    pointers are there you have to clone that linked list
    -- craete a clone list using original list - pahle next pointer se copy kare
    -- for random pointer we go to first vaha se find the distance of random pointer by loop. Inside me ek while loop jo us distance tak ja ke point kare jiski Tc = O(n2)
    
    
    Approach2 -- O(n) O(n)
        -- pahle clone list using next pointer
        -- random link karne ke liye - 
            mapping the original node with clone node with their pointer - {a:x,b:y,c:z}
            check the val of random of original node.let a.random = c then find the map value of c. after that assign z to x.random 
            
    Approach3 - O(n) O(1) - don't use map only use the linking
        1. clone by next pointer
        2. mapping ko real kar dete hai. mean 
            original.next = clone
            clone.next = original.next
            # random pointer is constant
        3. clone me link the random pointer
            temp = original
            # temp.next will be clone
            temp.next.random = temp.random.next
        4. revert the changes done in step2
        
    
    
    
    
    
    

        
            

"""
class Node:
    def __init__(self,data) -> None:
        self.data = data 
        self.next = None
        self.arb = None # random pointer


# Approach2
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        
        # clone the list
        h = head
        c = Node(0)
        clone = c
        m = {None:None} # some time random is None
        while head:
            n = Node(head.data)
            m[head] = n
            c.next = n
            c = c.next
            head = head.next
            
        # clone random
        c = clone.next
        while h:
            c.arb = m[h.arb]
            c = c.next
            h = h.next
        return clone.next
            
          
# Approach3
class Solution:
    #Function to clone a linked list with next and random pointer.
    def copyList(self, head):
        # code here
        
        # clone the list
        h = head
        c = Node(0)
        clone = c 
        while h:
            n = Node(h.data)
            c.next = n
            c = c.next
            h = h.next
        
        clone = clone.next
        
        originalNode = head
        cloneNode = clone
        while originalNode and cloneNode:
            next = originalNode.next
            originalNode.next = cloneNode
            originalNode = next
            
            next = cloneNode.next
            cloneNode.next = originalNode
            cloneNode = next
        
        # clone random
        temp = head
        while temp:
            if temp.next != None:
                if temp.arb !=None:
                    temp.next.arb = temp.arb.next
                else:
                    temp.next.arb = None
                    
            temp = temp.next.next
                
        # revert  change of step2
        originalNode = head
        cloneNode = clone
        while originalNode and cloneNode:
            originalNode.next = cloneNode.next
            originalNode = originalNode.next
            
            if originalNode != None:
                cloneNode.next = originalNode.next
            cloneNode = cloneNode.next
            
            
            
        return clone
                
            
            