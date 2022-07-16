

"""

There are many approach to solve the merge sort
    - By the help of two function first binary divide second is merge them.
        By parsing two array in binary devide and using new array to store the value
        By the help of one array and change in start and end position
 ** - By the help of one function and use another two variable and merge in same function


Uses of Merge Sort - It is used in linked list sorting



"""


def MergeSortInOneFunc(arr):
    
    start = 0
    end = len(arr)
    
    if end <= 1:
        return
    
    # parting the array
    mid = (start+end)//2
    left = arr[:mid]
    right = arr[mid:]
     
    #  merge sort in each part
    MergeSortInOneFunc(left)
    MergeSortInOneFunc(right)
    
    
    # merging both array
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[start] = left[i]
            i += 1
        else:
            arr[start] = right[j]
            j += 1
        start += 1
    
    # if any index left in left
    while i < len(left):
        arr[start] = left[i]
        start += 1
        i += 1
    # if any index left in right
    while j < len(right):
        arr[start] = right[j]
        start += 1
        j += 1
    return arr
            
            
def MergeSortTwoFunc(arr):
    if len(arr) <= 1:
        return arr
    
    mid = len(arr)//2
    return  merge(MergeSortTwoFunc(arr[:mid]),MergeSortTwoFunc(arr[mid:]))

def merge(left,right):
    newArr = []
    left.append(0)
    right.append(0)
    i = 0
    j = 0  
    for i in range(len(left)+len(right)):
        if left[i] < left[j]:
            newArr.append(left[i])
            i += 1
        else:
            newArr.append(right[j])
            j+= 1
            
    return newArr


if __name__ == "__main__":
    
    arr = [4,5,86,64,3,8,2,9,4,6,145,7]
    arr = [7,4,8,1,3,9,4]
    # print(merge([4,7,8,1,3,9]))

    print(MergeSortTwoFunc(arr))







# class Node:
    
#     def __init__(self,val = 0,next = None) -> None:
#         self.val = val
#         self.next = next
    
# def create(arr1,arr2):
#     l1 = Node()
#     l2 = Node()
#     a = l1
#     b = l2
#     for i in arr1:
#         a.val = i
#         a.next = Node()
#         a = a.next
#     for i in arr2:
#         b.val = i
#         b.next = Node()
#         b = b.next
#     return l1,l2
    
# def printNode(l):
#     li = []
#     while l:
#         li.append(l.val)
#         l = l.next
#     print(li)
#     return li


# # def MergeLinkedList(l1,l2):
# #     d = l1
# #     i = 0
# #     j = 0
# #     print(l1.val , l2.val)
# #     if l1.val > l2.val:
# #         k = l2.next
# #         l2.next = l1
# #         l1 = l2
# #         l2 = k
# #     printNode(l1)
# #     printNode(l2)
# #     print("ii")
# #     k = l1
# #     for _ in range(2):
# #         printNode(l2)
# #         print(l1.next.val , l2.next.val)
# #         print("came")
# #         printNode(k)
# #         if l1.next.val > l2.next.val:
# #             print("\nop")
# #             k = l1.next
# #             l1.next = l2.next
# #             l2.next = l2.next.next
# #             l1.next.next = k
            
            
# #         l1 = l1.next
# #     printNode(l2)
# #     return k

# # if __name__ == "__main__":
# #     arr1 = [4,5,8]
# #     arr2 = [2,2,3,9]
# #     l1,l2 = create(arr1,arr2)
# #     # printNode(l1)
# #     # printNode(l2)
# #     printNode(MergeLinkedList(l1,l2))
    
    