# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def removeKthNodeFromEnd(head, k):
    # Write your code here.
    # two pointers
    # the second pointer starts moving until the first pointer moves k steps
    pointer1 = pointer2 = LinkedList(None)
    pointer1.next = head
    pointer2.next = head
    while k > 0:
        pointer1 = pointer1.next
        k -= 1
    while pointer1.next:
        pointer1 = pointer1.next
        pointer2 = pointer2.next


        
    pointer2.next = pointer2.next.next
    if pointer2.value is None:
        head.value = head.next.value
        head.next = head.next.next
        return
    



