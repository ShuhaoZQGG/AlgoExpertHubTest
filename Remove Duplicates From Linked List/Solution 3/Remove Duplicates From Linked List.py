# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def removeDuplicatesFromLinkedList(linkedList):
    # Write your code here.
    Dummy = linkedList
    while Dummy.next:
        if Dummy.value == Dummy.next.value:
            Dummy.next = Dummy.next.next
        else:
            Dummy = Dummy.next
    return linkedList

