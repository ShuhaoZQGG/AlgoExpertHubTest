<pre>
Solution1:
Idea: Iterate through all the values, search for the minimum of abs(target - node.value)

1. create a stack, save tree into the stack
2. pop off one node each time, check if it is the closest value so far, if so, update the closest value
3. push node.left and node.right into the stack, continue the process
4. end the iteration when there is no node left, ex: self.value = null, self.right = null, self.left = null, return closest_value
</pre>