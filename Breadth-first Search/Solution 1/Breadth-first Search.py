from collections import deque
# Do not edit the class below except
# for the breadthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name


    def addChild(self, name):
        self.children.append(Node(name))
        return self


    def breadthFirstSearch(self, array):
        # Write your code here.
        q = deque([self])
        while q:
            node = q.popleft()
            array.append(node.name)
            for i in range(len(node.children)):
                q.append(node.children[i])
        return array

