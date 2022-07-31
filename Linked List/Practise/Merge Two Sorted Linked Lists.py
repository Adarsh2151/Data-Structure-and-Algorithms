
link = "https://www.codingninjas.com/codestudio/problems/merge-two-sorted-linked-lists_800332"

"""
Merge two sorted linked list
    - if head1 == None:
        return head2
    - if head2 == None:
        return head1
    
    
    hamesa take from dusiri linked list and check wheather it come between i and i+ 1 :
    Agar nahi to update current to next
    if came then check for next in head2



"""

# Following is the linked list node structure:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
      
def sortTwoLists(first, second):
    # Write your code here.
    
    # Base Case
    if first == None:
        return second
    if second == None:
        return first
        
    
    if first.data < second.data:  # first will start from greater than second start
        first , second = second , first

    # Pointers for first and second Node
    curr = first
    temp = second
    
    
    while curr:  # for first ll 
        k = curr.next
        while temp.next:  # in second ll
            if temp.data <= curr.data <=temp.next.data:  # condition to add in between
                curr.next = temp.next
                temp.next = curr
                break  # we assign don't need to go ahead
            temp = temp.next # temp will be assigned global because agar jaha tak assign kar chuke honge uske bad hi assign karna hai. kyoki linked list sorted hai.
            
        if temp.next == None:   # this is for adding at end 
            temp.next = curr
            break  # break is neccesary because no extra to assign after it . you can use None .
         
        curr = k

    return second





