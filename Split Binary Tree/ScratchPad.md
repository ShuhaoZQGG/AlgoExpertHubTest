<pre>1. for each node, calculate the sum of its left branch and right branch
2. there are two possibilities for each node: node.value + left branch = right branch
OR node.value + right branch = left branch
3. if there is any node whose split edges' sums are equal, return the sum
4. if not found after searching through all the nodes, return 0
5. the time complexity is O(2 * n) (2 checks for each node) and space complexity is O(n)</pre>