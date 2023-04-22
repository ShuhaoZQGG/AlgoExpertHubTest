# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def splitBinaryTree(tree):
    # Write your code here.
    total_sum = sum_binary_tree(tree)
    
    # helper function to recursively check if the binary tree can be split
    def traverse(node):
        if not node:
            return False
        
        # calculate the sum of the left and right subtrees
        left_sum = sum_binary_tree(node.left)
        right_sum = sum_binary_tree(node.right)
        
        # check if the current node can be removed to split the tree into two equal parts
        if left_sum == total_sum - left_sum or right_sum == total_sum - right_sum:
            return True
        
        # recursively check if the left or right subtree can be split
        return traverse(node.left) or traverse(node.right)
    
    # check if the tree can be split and return the new sum of each binary tree
    if traverse(tree):
        return total_sum // 2
    else:
        return 0
        
def sum_binary_tree(root: BinaryTree) -> int:
    if not root:
        return 0


    left_sum = sum_binary_tree(root.left)
    right_sum = sum_binary_tree(root.right)


    return root.value + left_sum + right_sum