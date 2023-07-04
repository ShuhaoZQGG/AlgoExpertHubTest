def allKindsOfNodeDepths(root, totalDepth = 0):
    # Write your code here.
    def getDepth(node):
        depth = 0
        q = [(node, 0)]
        while q:
            n, lvl = q.pop()
            depth += lvl
            if n.left:
                q.append((n.left, lvl + 1))
            if n.right:
                q.append((n.right, lvl + 1))
        return depth
    totalDepth = 0
    q = [root]
    if root:
        totalDepth += getDepth(root)
        if root.left:
            totalDepth += allKindsOfNodeDepths(root.left, totalDepth)
        if root.right:
            totalDepth += allKindsOfNodeDepths(root.right, totalDepth)
    return totalDepth
# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

