import math
def findClosestValueInBst(tree, target):
    # Write your code here.
    minValue = math.inf
    def dfs(tree, minValue):
        if not tree:
            return minValue


        if abs(target - tree.value) < abs(target - minValue):
            minValue = tree.value


        if target > tree.value:
            return dfs(tree.right, minValue)
        elif target < tree.value:
            return dfs(tree.left, minValue)
        return minValue
    return dfs(tree, minValue)
# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

