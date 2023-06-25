from collections import deque
# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


# 1. find target node given the value
# 2. assign parent node to each node
# 3. traverse through node.left, node.right and node.parent to find matched nodes with distance k
def findNodesDistanceK(tree, target, k):
    # Write your code here.
    parentNodes = dict()
    visited = set()
    targetNode = [None]
    output = []
    
    def findTargetNodeAndAssignParent(node, parentNode = None):
        if not node:
            return
        if node.value == target:
            targetNode[0] = node
        parentNodes[node.value] = parentNode
        findTargetNodeAndAssignParent(node.left, node) # node would be the parent of node.left and node.right
        findTargetNodeAndAssignParent(node.right, node)
    findTargetNodeAndAssignParent(tree)
    queue = deque([(targetNode[0], 0)]) # (node, distance)
    while queue:
        node, distance = queue.popleft()
        if distance == k:
            output.append(node.value)
        if node.value not in visited:
            visited.add(node.value)
        for neighbour in [node.left, node.right, parentNodes[node.value]]:
            if neighbour:
                if neighbour.value not in visited:
                    queue.append((neighbour, distance + 1))
    return output