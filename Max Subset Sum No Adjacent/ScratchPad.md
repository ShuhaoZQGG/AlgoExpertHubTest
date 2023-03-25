<pre>
array = [75, 105, 120, 75, 90, 135]

non-adjacent:
1. [75 120 90 150]
2. [105 75 135 100 80]

start from 75:
75 + 120 + 90 + 150 + 80
75 + 


75 0 0
0 0 0
0 0 0

Idea of Solution1:
At any point n, there are only two options for the next move: value(n) + value(n+2) or value(n) + value(n+3)
because: value(n) + value(n+4) = value(n) + value(n+2) + value(n+2) 
so we can have a tree diagram:

        0
      75 105
    120 75 75 90
90 135 135 

find every possibilty and find the maximum value
time_complexity: 2^n

Solution 2:
find maximum value at each index i solution(i):
original: [75 105 120 75 90 135]
maximum: [75 105 195 195 285 330]

we can find that:
base case: i = 0 max = array[0]
i = 1: max = max(array[0], array[1])
</pre>