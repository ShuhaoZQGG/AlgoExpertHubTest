<pre>solution 1:
insert inorder values into an array, find the node at i and return arr[i+1]

solution 2:
inorder: left - visit - right
if a node has a right sub tree, its successor must be at the left most child of its right sub tree
if a node doesn't have a right sub tree, its successor would be the ancestor (from the tree perspective) which contains this node at its left subtree</pre>