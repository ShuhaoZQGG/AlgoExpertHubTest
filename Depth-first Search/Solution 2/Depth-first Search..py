# Do not edit the class below except
# for the depthFirstSearch method.
# Feel free to add new properties
# and methods to the class.
from collections import deque
class Node:
    def __init__(self, name):
        self.children = []
        self.name = name


    def addChild(self, name):
        self.children.append(Node(name))
        return self


    def depthFirstSearch(self, array):
        # Write your code here.
        queue = deque([self])
        while queue:
            node = queue.pop()
            array.append(node.name)
            if node:
                for child in node.children[::-1]:
                    queue.append(child)
        return array

