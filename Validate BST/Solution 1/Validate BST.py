import math


# This is an input class. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None




def validateBst(tree):
    # Write your code here.
    def validate(node, minVal, maxVal):
        if node is None:
            return True
            
        if node.value < minVal:
            return False


        if node.value >= maxVal:
            return False
        
        validateRight =  validate(node.right, node.value, maxVal)
        validateLeft = validate(node.left, minVal, node.value)


        if validateRight and validateLeft:
            return True
        else:
            return False
    


    return validate(tree, -math.inf, math.inf)

