from ll import LinkedList

link = "https://www.codingninjas.com/codestudio/problems/reverse-list-in-k-groups_983644"


"""
Approach -- 
    Reverse in group in "
    use recursion - we reverse first k node and call recursively
    Time complexity - O(n) space complexity - O(n)

"""


def reverseKgroup(head,k):
    #Base case
    if head == None:
        return None
    # simple reverse up to k level
    prev = None
    h = head
    l = 0
    while h and l<k:
        forward = h.next
        h.next = prev
        prev = h
        h = forward
        l+=1
    
    # recursive call
    if forward != None:
        head.next = reverseKgroup(forward,k)
    
    return prev





if __name__ == "__main__":
    a = LinkedList(4)
    a.append(1)
    a.append(2)
    a.append(3)
    a.append(4)
    a.append(5)
    a.append(6)
    a.append(7)
    Y = reverseKgroup(a.head,2)
    a.head = Y
    a.print()