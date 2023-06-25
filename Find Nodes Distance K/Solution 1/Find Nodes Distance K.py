from collections import deque
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def findNodesDistanceK(tree, target, k):
    # Write your code here.
    result = []
    parentNodes = {}
    targetNode = [None]
    visited = set()
    def preorder(node, parent=None):
        if not node:
            return
        if target == node.value:
            targetNode[0] = node
        parentNodes[node.value] = parent


        
        preorder(node.left, node)
        preorder(node.right, node)


    preorder(tree)
    queue = deque([(targetNode[0], 0)])
    while queue:
        node, dist = queue.popleft()
        visited.add(node.value)
        if dist == k:
            result.append(node.value)
        for neighbour in [node.left, node.right, parentNodes[node.value]]:
            if neighbour:
                if neighbour.value not in visited:
                    queue.append((neighbour, dist + 1))


    return result