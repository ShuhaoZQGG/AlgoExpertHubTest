# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def mergeLinkedLists(headOne, headTwo):
    # Write your code here.
    ptr1, ptr2 = headOne, headTwo
    if ptr1.value > ptr2.value:
        ptr1, ptr2 = ptr2, ptr1
    dummy = prevPtr1 = ptr1
    while ptr1 and ptr2:
        nextPtr1 = ptr1.next
        nextPtr2 = ptr2.next
        if ptr1.next and ptr1.next.value > ptr2.value:
            ptr1.next = ptr2
            ptr2.next = nextPtr1
            ptr2 = nextPtr2
        prevPtr1 = ptr1
        ptr1 = ptr1.next
    if not(ptr1) and ptr2:
        prevPtr1.next = ptr2


    return dummy
        

