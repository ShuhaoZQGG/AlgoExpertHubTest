from collections import deque
def nodeDepths(root):
    # Write your code here.
    ans = 0
    stack = deque([(root, 0)])
    while stack:
        node, value = stack.popleft()
        if node:
            ans += value
            stack.append((node.left, value + 1))
            stack.append((node.right, value + 1))
    return ans
    




# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

