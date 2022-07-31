
link = "https://www.codingninjas.com/codestudio/problems/circularly-linked_1070232"

"""
1. A linked list is said to be circular if it has no node having its next pointer equal to NULL and all the nodes form a circle i.e. the next pointer of last node points to the first node.
2. An empty linked will also be considered as circular.
3. All the integers in the linked list are unique.
4. In the input, the next pointer of a node with i’th integer is linked to the node with data (i+1)’th integer (If (i+1)’th node exists). If there is no such (i+1)’th integer then the next pointer of such node is set to NULL.


For Better understanding read the code

"""

def isCircular(head):
    # Write your code here
    if head == None:
        return True
    h = head
    
    d = dict()
    while head:
        if (d.setdefault(head.next,False)):
            if head.next == h:
                return True
            return False
        d[head] = True
        head = head.next
    return False



if __name__ == "__main__":
    
    
    pass
