<pre>Parameters:
k: number of workers
tasks: an array of tasks, each element represent the time to complete each task
length of tasks = 2 * k (each worker must complete 2 tasks)
each worker can only do one task at a time (sequentially)

example:
k = 3
tasks = [1 3 5 3 1 4]

return an optimal 2d list of assigned tasks (least amount of time)
[
[0 2]
[4 5]
[1 3]
]

solution 1:
sort the list, match list[0] to list[n-1], list[1] to list[n-2] ...</pre>