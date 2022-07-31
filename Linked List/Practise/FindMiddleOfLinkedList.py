link = "https://www.codingninjas.com/codestudio/problems/middle-of-linked-list_973250"

"""
We have many approach to sove it - first get len and find the mid element. then help of iteration return that index. second take two variable that one goes with speed of 1 another with speed of 1.

we can think one pointer move with speed of 2 and another with speed of one that one is our answer.


"""
def findMiddle(head):
    # Write your code here
    # head denoted head of linked list
    i = head
    j = 1  # one for odd entity
    while head:
        if j != 0 and j%2 == 0:
            i = i.next
        head = head.next
        j += 1
    return i
        
