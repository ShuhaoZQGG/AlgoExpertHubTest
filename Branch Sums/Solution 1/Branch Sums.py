# This is the class of the input root. Do not edit it.
class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
def branchSums(root):
    # Write your code here
    q = [(root, 0)]
    ans = []
    while q:
        node, sum = q.pop()
        if node:
            sum += node.value
            q.append((node.right, sum))
            q.append((node.left, sum))
            if node.left is None and node.right is None:
                ans.append(sum)
    return ans
    
    