# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def middleNode(linkedList):
    # Write your code here.
    # 1. return the middle node if the linkedList is odd size
    # 2. return the 2nd middle node if the linkedList is even size
    # Two pointers, 1st pointer moves at the speed of 2, 2nd pointer movest at the speed of 1
    # 2 => 7 => 3 => 5
    # 1st pointer None 2nd pointer None
    #             7                  2
    #             5                  7
    # now 1st pointer.next is None, we know it reaches end, and the size is even, 2nd pointer = 2nd pointer.next


    # 2 => 7 => 3 => 5 => 10
    # None None
    # 7     2
    # 5     7
    # 5.next = 10, 5.next.next = None, we know it reaches the end, and the size is odd, 2nd pointer = 2nd pointer.next
    pointer1, pointer2 = LinkedList(None), LinkedList(None)
    pointer1.next = linkedList
    pointer2.next = linkedList
    while pointer2.next and pointer2.next.next:
        pointer2 = pointer2.next.next
        pointer1 = pointer1.next
    return pointer1.next

