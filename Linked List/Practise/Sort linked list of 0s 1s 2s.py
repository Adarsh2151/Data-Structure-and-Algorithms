link = "https://www.codingninjas.com/codestudio/problems/sort-linked-list-of-0s-1s-2s_1071937"


# Given a problem - A linked list of consist of value 0,1,2 in any order in any times .Your Task is to sort them


"""
Approach1 - first find the occuretion of each and use loop and assign all to    their occuration by data replace


*Approach2 -- Without data replacement
    create three linked list node of (1,2,3)
    merge all of them



"""





#  Aproach by Replace data method of O(n)

def sortList(head):
    # Write your code here
    z = 0
    o = 0
    t = 0
    h = head
    while h:
        if h.data == 0:
            z+=1
        if h.data == 1:
            o+= 1
        if h.data == 2:
            t += 1
        h = h.next
    k = head
    while k:
        if z != 0:
            k.data = 0
            z-= 1
        elif o != 0:
            k.data =1
            o -= 1
        else:
            k.data = 2
            t -= 1
        k = k.next
    return head




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
# Approach by refrencing linked list
        
def sortList(head):
    # Write your code here
    # why dummy node : nahi to if condition lagana prega
    z = Node(0)
    o = Node(0)
    t = Node(0)
    a,b,c = z,o,t
    h = head
    while h:
        if h.data == 0:
            a.next = Node(h.data)
            a = a.next
        if h.data == 1:
            b.next = Node(h.data)
            b = b.next
        if h.data == 2:
            c.next = Node(h.data)
            c = c.next
        h = h.next
    a.next = o.next
    b.next = t.next
    head = z.next
    
    
#      delete pointers
    del a
    del b
    del c
    del z
    del o
    del t
    
    return head
    
    