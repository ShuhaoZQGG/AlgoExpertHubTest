# This is an input class. Do not edit.
class BST:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right




def validateThreeNodes(nodeOne, nodeTwo, nodeThree):
    # Write your code here.
    return (validateTwoNodes(nodeOne, nodeTwo) and validateTwoNodes(nodeTwo, nodeThree)) or (validateTwoNodes(nodeThree, nodeTwo) and validateTwoNodes(nodeTwo, nodeOne))
    
def validateTwoNodes(ancestorNode, descendantNode):
    if ancestorNode == descendantNode:
        return True
    if ancestorNode is None:
        return False
    if descendantNode.value > ancestorNode.value:
        ancestorNode = ancestorNode.right
    else:
        ancestorNode = ancestorNode.left
    return validateTwoNodes(ancestorNode, descendantNode)

