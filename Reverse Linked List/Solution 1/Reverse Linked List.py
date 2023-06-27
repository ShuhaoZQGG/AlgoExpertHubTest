# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def reverseLinkedList(head):
    # Write your code here.
    p1, p2 = None, head
    while p2:
        nextPtr = p2.next
        p2.next = p1
        p1 = p2
        p2 = nextPtr
    return p1