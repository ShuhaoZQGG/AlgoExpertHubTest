# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def shiftLinkedList(head, k):
    # Write your code here.
    ptr1 = head
    length = 1
    while ptr1.next:
        length += 1
        ptr1 = ptr1.next
    normK = k % length
    k = length - normK
    if k == length or k == 0:
        return head
    ptr1.next = head




    while k > 0:
        k -= 1
        ptr1 = ptr1.next
    newHead = ptr1.next
    ptr1.next = None
    return newHead