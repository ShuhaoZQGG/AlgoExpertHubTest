import math
def findClosestValueInBst(tree, target):
    # Write your code here.
    closest_value = math.inf
    q = [tree]
    while q:
        node = q.pop()
        if min(abs(target - closest_value), abs(target - node.value)) == abs(target - closest_value):
            closest_value = closest_value
        else:
            closest_value = node.value
        if node.right:
            q.append(node.right)
        if node.left:
            q.append(node.left)
    
    return closest_value




# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

