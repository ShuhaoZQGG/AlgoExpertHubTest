# Min Number Of Jumps


  You're given a non-empty array of positive integers where each integer represents the
  maximum number of steps you can take forward in the array. For example, if the
  element at index 1 is 3, you can go from index
  1 to index 2, 3, or 4.


  Write a function that returns the minimum number of jumps needed to reach the
  final index.


  Note that jumping from index i to index i + x always
  constitutes one jump, no matter how large x is.

**Sample Input**
array = [3, 4, 2, 1, 2, 3, 7, 1, 1, 1, 3]

**Sample Output**
4 // 3 --> (4 or 2) --> (2 or 3) --> 7 --> 3

# Find Closest Value In BST


  Write a function that takes in a Binary Search Tree (BST) and a target integer
  value and returns the closest value to that target value contained in the BST.

You can assume that there will only be one closest value.

  Each BST node has an integer value, a
  left child node, and a right child node. A node is
  said to be a valid BST node if and only if it satisfies the BST
  property: its value is strictly greater than the values of every
  node to its left; its value is less than or equal to the values
  of every node to its right; and its children nodes are either valid
  BST nodes themselves or None / null.

**Sample Input**
tree =   10
       /     \
      5      15
    /   \   /   \
   2     5 13   22
 /           \
1            14
target = 12

**Sample Output**
13
# Array Of Products


  Write a function that takes in a non-empty array of integers and returns an
  array of the same length, where each element in the output array is equal to
  the product of every other number in the input array.


  In other words, the value at output[i] is equal to the product of
  every number in the input array other than input[i].

Note that you're expected to solve this problem without using division.
**Sample Input**
array = [5, 1, 4, 2]

**Sample Output**
[8, 40, 10, 20]
// 8 is equal to 1 x 4 x 2
// 40 is equal to 5 x 4 x 2
// 10 is equal to 5 x 1 x 2
// 20 is equal to 5 x 1 x 4

# Four Number Sum


  Write a function that takes in a non-empty array of distinct integers and an
  integer representing a target sum. The function should find all quadruplets in
  the array that sum up to the target sum and return a two-dimensional array of
  all these quadruplets in no particular order.


  If no four numbers sum up to the target sum, the function should return an
  empty array.

**Sample Input**
array = [7, 6, 4, -1, 1, 2]
targetSum = 16

**Sample Output**
[[7, 6, 4, -1], [7, 6, 1, 2]] // the quadruplets could be ordered differently

