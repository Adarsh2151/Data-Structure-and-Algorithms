from ll import LinkedList

link = "https://www.codingninjas.com/codestudio/problems/unique-sorted-list_2420283"
link = "https://www.codingninjas.com/codestudio/problems/remove-duplicates-from-unsorted-linked-list_1069331"

""" 
Approaach
    for sorted linked list
        There is a simple approach that go n times if next is equal then refrence it to next.next
        o(N),O(1)
    for unsorted linked list
        for every index traverse the linked list and delete the duplicates -- O(n2)
        
        first sort in nlogn and remove duplicate by n -- O(nlogn)
        
        use map and a loop  --  O(n),o(n)


"""

def uniqueSortedList(head):
    # write your code here
    if head == None:
        return head
    h = head
    while h.next:
        if h.data == h.next.data:
            h.next = h.next.next
        else:    
            h = h.next
    return head
            
            
def removeDuplicates(head):
    curr = head
    
    while curr:
        
        temp  = curr
        
        while temp.next:
            if curr.data == temp.data:
                temp.next = temp.next.next
            temp = temp.next
        curr = curr.next
        return head
            
    






def pri(a):
    aa = []
    while a != None:
        aa.append(a.data)
        a = a.next 
    print(aa)
               



if __name__ == "__main__":
    a = LinkedList(1)
    a.append(2)
    a.append(2)
    a.append(2)
    a.append(3)
    a.append(5)
    a.append(5)
    a.append(5)
    a.append(7)
    
    # re = uniqueSortedList(a.head)
    # a.head = re
    # a.print()
    b = LinkedList(4)
    b.append(2) 
    b.append(5) 
    b.append(4) 
    b.append(2) 
    b.append(2) 
    b.print()
    u  = removeDuplicates(b.head)
    print("FFFFFF\n\n")
    b.head = u
    b.print()