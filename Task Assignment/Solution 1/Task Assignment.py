def taskAssignment(k, tasks):
    # Write your code here.
    map = {}
    n = len(tasks)
    for i in range(n):
        if tasks[i] not in map:
            map[tasks[i]] = [i]
        else:
            map[tasks[i]].append(i)


    ans = []
    tasks.sort()
    for i in range(n//2):
        task1 = map[tasks[i]][0]
        task2 = map[tasks[n - i - 1]][0]
        del map[tasks[i]][0]
        del map[tasks[n - i - 1]][0]
        ans.append([task1, task2])
    return ans