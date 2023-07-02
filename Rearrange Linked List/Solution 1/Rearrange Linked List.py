# This is the class of the input linked list.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def rearrangeLinkedList(head, k):
    # Write your code here.
    smaller, larger = [], []
    ptr = head
    firstNodeK = findNode(head, k)
    nextNodeK = findNode(head, k)
    if firstNodeK:
        while ptr:
            if ptr.value == k:
                if ptr is not nextNodeK:
                    nextNodeK.next = ptr
                    nextNodeK = nextNodeK.next
                ptr = ptr.next
            else:
                if ptr.value < k:
                    smaller.append(ptr)
                else:
                    larger.append(ptr)
                nextPtr = ptr.next
                ptr.next = None
                ptr = nextPtr
        smallerHead, smallerTail = create_linked_list(smaller)
        largerHead, largerTail = create_linked_list(larger)
        if largerHead:
            nextNodeK.next = largerHead
        if smallerTail:
            smallerTail.next = firstNodeK
            return smallerHead
        return firstNodeK
    else:
        while ptr:
            if ptr.value < k:
                smaller.append(ptr)
            else:
                larger.append(ptr)
            nextPtr = ptr.next
            ptr.next = None
            ptr = nextPtr
        smallerHead, smallerTail = create_linked_list(smaller)
        largerHead, largerTail = create_linked_list(larger)
        if smallerTail:
            smallerTail.next = largerHead
            return smallerHead
        elif smallerHead:
            smallerHead.next = largerHead
            return smallerHead
        else:
            return largerHead


    
    
def findNode(head, k):
    node = head
    while node:
        if node.value == k:
            return node
        node = node.next
    return None


def create_linked_list(arr):
    if not arr:
        return (None, None)


    head = arr[0]
    current = head


    for i in range(1, len(arr)):
        new_node = arr[i]
        current.next = new_node
        current = new_node
    
    return (head, current)



