# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def sumOfLinkedLists(linkedListOne, linkedListTwo):
    # Write your code here.
    linkedListOneStr = linkedListToStr(linkedListOne)
    linkedListTwoStr = linkedListToStr(linkedListTwo)
    linkedListSum = str(int(linkedListOneStr) + int(linkedListTwoStr))
    ptr = dummy = LinkedList(None)
    for c in reversed(linkedListSum):
        dummy.next = LinkedList(int(c))
        dummy = dummy.next
    return ptr.next
    
def linkedListToStr(linkedList):
    outputStr = ''
    while linkedList.next:
        outputStr = str(linkedList.value) + (outputStr)
        linkedList = linkedList.next
    outputStr = str(linkedList.value) + (outputStr)
    return outputStr



