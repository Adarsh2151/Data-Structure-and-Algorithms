
#  Stack Using Linked List 

class Node:
    def __init__(self,data = None) -> None:
         self.data = data
         self.next = None
         

class Stack:
    def __init__(self) -> None:
        self.top = None

    def pushBack(self,data):
        if self.top == None:
            ne = Node(data)
            self.top = ne
            return ;
            
        ne = Node(data)
        ne.next = self.top
        self.top = ne
        
    def popBack(self):
        if self.top == None or self.top.next == None:
            self.top = None
            return 
        self.top = self.top.next
    
    def peek(self):
        if self.top == None:
            return None
        return self.top.data
    
    def isEmpty(self):
        return True if self.top == None else False
    
    
    #  Extra method to print out all element of stack
    def pr(self):
        t = self.top
        while t:
            print(t.data)
            t = t.next


if __name__ == "__main__":
    l = Stack()   
    print(l.peek())
    print(l.isEmpty())  
    l.popBack()    
    l.pushBack(1)  
    l.pushBack(2)
    print(l.peek())
    print(l.isEmpty())  
    l.popBack()
    l.pushBack(32)  
    l.pushBack(38)  
    l.pr()




# Using Double LInked List

"""
class Node:
    def __init__(self,data = None) -> None:
         self.data = data
         self.next = None
         self.prev = None
         

class Stack:
    def __init__(self) -> None:
        self.tail = None
        self.head = None

    def pushBack(self,data):
        if self.head == None:
            ne = Node(data)
            self.head = ne
            self.tail = ne
            
        ne = Node(data)
        ne.prev = self.tail
        self.tail = ne
        
    def popBack(self):
        if self.tail == None or self.tail.prev == None:
            self.tail = None
            return 
        self.tail.prev.next = None
        self.tail = self.tail.prev
    
    def peek(self):
        if self.tail == None:
            return None
        return self.tail.data
    
    def isEmpty(self):
        return True if self.tail == None else False
    
    
    #  Extra method to print out all element of stack
    def pr(self):
        t = self.tail
        while t:
            print(t.data)
            t = t.prev

l = Stack()   
print(l.peek())
print(l.isEmpty())  
l.popBack()    
l.pushBack(1)  
l.pushBack(2)
print(l.peek())
print(l.isEmpty())  
l.popBack()
l.pushBack(32)  
l.pushBack(38)  
l.pr()



"""