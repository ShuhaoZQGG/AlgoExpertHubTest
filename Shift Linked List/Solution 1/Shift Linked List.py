# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def shiftLinkedList(head, k):
    # Write your code here.
    if k == 0:
        return head
    length = 1
    ptr1 = head
    while ptr1.next:
        length += 1
        ptr1 = ptr1.next


    normK = k % length


    if normK == 0:
        return head


    ptr1.next = head
    k = length - normK
    


    newHead = LinkedList(None)
    
    for i in range(0,  k + 1):
        if (i == k):
            newHead = ptr1.next
            ptr1.next = None
        ptr1 = ptr1.next


    return newHead
# def getLength(ll):
#     counter = 0
#     while ll:
#         counter += 1
#         ll = ll.next
#     return counter