# This is an input class. Do not edit.
class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None




def findLoop(head):
    # Write your code here.
    slow, quick = head.next, head.next.next
    while slow is not quick:
        slow = slow.next
        quick = quick.next.next


    answer = head
    while answer is not slow:
        answer = answer.next
        slow = slow.next
    return answer