<pre>Thought:
1. recursion
2. recursive step: a tree with only one root and two (or one) leaf nodes
ex: 2                    2
/   \     =>         /   \
1      3             3      1

root doesn't change, swap left and right child

3. base case: a tree with no children, just return the tree
4. keep recursing until met the base case
</pre>