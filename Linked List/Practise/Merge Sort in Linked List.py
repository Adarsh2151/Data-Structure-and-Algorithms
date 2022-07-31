
link = "https://www.codingninjas.com/codestudio/problems/mergesort-linked-list_630514"
""" 
Given a linked list you have to sort them by merge sort without replace of data only change link
"""


""" 
Approach - O(logn),O(n)
    devide the merge sort in 2 equal part
    use the code of merge sorted algorithm

"""




class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def getMid(head):
    if head == None:
        return head
    i = head
    j = head
    while i.next and i.next.next:
        i = i.next.next
        j = j.next
    return j


def merge(first, second):
    if first == None:
        return second
    if second == None:
        return first
    newNode = Node(-1)
    temp = newNode
    
    while first and second:
        if first.data < second.data:
            temp.next = first
            temp = first
            first = first.next
        else:
            temp.next = second
            temp = second
            second = second.next
            
    while first:
        temp.next = first
        temp = first
        first = first.next
    while second:
        temp.next = second
        temp = second
        second = second.next

    return newNode.next


        
def mergeSort(head):
    # Write your code here.
    if head == None or head.next == None:
        return head
    mid = getMid(head)
    right = mid.next
    mid.next = None
    left = head

    left = mergeSort(left)
    right = mergeSort(right)
    result = merge(left,right)
    return result








