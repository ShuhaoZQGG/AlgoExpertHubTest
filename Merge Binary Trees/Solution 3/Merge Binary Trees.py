# This is an input class. Do not edit.
class BinaryTree:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def mergeBinaryTrees(tree1, tree2):
    # Write your code here.
    tree1Stack = [tree1]
    tree2Stack = [tree2]
    while tree1Stack:
        nodeTree1 = tree1Stack.pop()
        nodeTree2 = tree2Stack.pop()
        if nodeTree2 is None:
            continue
        nodeTree1.value += nodeTree2.value


        if not nodeTree1.left:
            nodeTree1.left = nodeTree2.left
        else:
            tree1Stack.append(nodeTree1.left)
            tree2Stack.append(nodeTree2.left)
        if not nodeTree1.right:
            nodeTree1.right = nodeTree2.right
        else:
            tree1Stack.append(nodeTree1.right)
            tree2Stack.append(nodeTree2.right)
    return tree1

