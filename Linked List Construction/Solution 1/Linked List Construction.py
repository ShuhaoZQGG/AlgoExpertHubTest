# This is an input class. Do not edit.
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None




# Feel free to add new properties and methods to the class.
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None


    def setHead(self, node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            self.insertBefore(self.head, node)
        
    def setTail(self, node):
        # Write your code here.
        if self.tail is None:
            self.setHead(node)
        else:
            self.insertAfter(self.tail, node)


    def insertBefore(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert != self.head or nodeToInsert != self.tail:
            self.remove(nodeToInsert)
            nodeToInsert.prev = node.prev
            nodeToInsert.next = node
            if node.prev is None:
                self.head = nodeToInsert
            else:
                node.prev.next = nodeToInsert
            node.prev = nodeToInsert
            
    def insertAfter(self, node, nodeToInsert):
        # Write your code here.
        if nodeToInsert != self.head or nodeToInsert != self.tail:
            self.remove(nodeToInsert)
            nodeToInsert.prev = node
            nodeToInsert.next = node.next
            if node.next is None:
                self.tail = nodeToInsert
            else:
                node.next.prev = nodeToInsert
            node.next = nodeToInsert


    def insertAtPosition(self, position, nodeToInsert):
        # Write your code here.
        node = self.head
        if position == 1:
            return self.setHead(nodeToInsert)
        while position > 1:
            node = node.next
            position -= 1
        if node:
            self.insertBefore(node, nodeToInsert)
        else:
            self.setTail(nodeToInsert)
            
    def removeNodesWithValue(self, value):
        # Write your code here.
        node = self.head
        while node:
            removed = node
            node = node.next
            if removed.value == value:
                self.remove(removed)


    def remove(self, node):
        # Write your code here.
        if node is self.head:
            self.head = self.head.next
        if node is self.tail:
            self.tail = self.tail.prev 
        if node.prev:
            node.prev.next = node.next
        if node.next:    
            node.next.prev = node.prev
        node.prev = None
        node.next = None
            


    def containsNodeWithValue(self, value):
        # Write your code here.
        node = self.head
        while node:
            if node.value == value:
                return True
            node = node.next
        return False

