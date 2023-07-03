def allKindsOfNodeDepths(root):
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
    while q:
        node = q.pop()
        depth = getDepth(node)
        totalDepth += depth
        if node.left:
            q.append(node.left)
        if node.right:
            q.append(node.right)
    return totalDepth


# This is the class of the input binary tree.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

