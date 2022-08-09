
link = "https://www.codingninjas.com/codestudio/problems/interview-shuriken-42-detect-and-remove-loop_241049"

""" 
Detect cycle in Linked List  -- floyd'a detection algorithm
Remove cycle in Linked List  -- At the last end of loop set value to null.
Output the start node of linked list -- get 

"""

""" 
Approachs -- 
    Given a linked list and detect cycle
    Approach1 - store all key to map and check it visted or not -- O(n),O(n)
    Approach2 - Floyd's cycle detection algorithm --  Take two pointer that one speed is   one and fast speed is 2 if they meet at any time then it has cycle. At every iteration in loop we reduce a distance from fast to slow.
 
 TODO : 5 way to remove cycle detection and 3 way to detect
"""

from ll import LinkedList

def detect(head):
    d = dict()
    while head:
        if (d.setdefault(head.next,False)):
            return head.data
        d[head] = True
        head = head.next
    
    
    pass

def floydDetect(head):
    fast = head;
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            return fast.data
        
def floydDetectBegin(head):
    fast = head;
    slow = head
    while fast:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            while head != fast:
                fast = fast.next
                head = head.next
            return fast.data

def removeLoop(head):
    fast = head;
    slow = head
    prev = None
    while fast and fast.next:
        prev = slow
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            if slow == head:
                prev.next = None
                return head
            slow = head
            prev = None
            while slow != fast:
                prev = fast
                slow = slow.next
                fast = fast.next
            prev.next = None
            return head
    return head


        
        
if __name__ == "__main__":
    a = LinkedList(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    a.print()
    a.head.next.next.next.next = a.head.next
    # a.print()
    print(detect(a.head))
    print(floydDetect(a.head))
    print(floydDetectBegin(a.head))
