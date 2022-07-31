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
        a = self.head
        while a != None:
            print(a.data)
            a = a.next 
    

