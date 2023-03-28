class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = BST(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = BST(value)
            else:
                self.right.insert(value)
                
def minHeightBst(array):
    return formBstTree(array, BST(None))
    
def formBstTree(array, tree):
    n = len(array) // 2
    if len(array) < 1:
        return tree
        
    if tree.value is None:
        tree = BST(array[n])
    else:
        tree.insert(array[n])
   


    del array[n]
    formBstTree(array[0:n], tree)
    formBstTree(array[n:len(array) + 1], tree)
    return tree