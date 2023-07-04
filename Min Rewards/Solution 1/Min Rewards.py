def minRewards(scores):
    # Write your code here.\
    if (len(scores)) == 1:
        return 1
    troughs = find_troughs(scores)
    map = {}
    total = 0
    troughs.sort(key=lambda x: x[2] - x[0], reverse=True)
    for trough in troughs:
        mini = 1
        start, troIndex, end = trough
        tro = scores[troIndex]
        if tro not in map:
            map[tro] = mini
            total += mini
        for i in range(troIndex, end + 1):
            el = scores[i]
            if el not in map:
                mini += 1
                map[el] = mini
                total += mini
        mini = 1
        for i in range(troIndex, start-1, -1):
            el = scores[i]
            if el not in map:
                mini += 1
                map[el] = mini 
                total += mini
    return total


def find_troughs(arr):
    troughs = []
    n = len(arr)


    i = 0
    start_index = i  
    end_index = i
    while i < n - 1:
        trough_index = i
        if i - 1 >= 0:
            if arr[i] < arr[i - 1] and arr[i] < arr[i + 1]:
                trough_index = i
                end_index = i


                while i < n - 1 and arr[i] <= arr[i + 1]:
                    i += 1


                end_index = i
                troughs.append((start_index, trough_index, end_index))
                start_index = i
        else:
            if arr[i] < arr[i + 1]:
                trough_index = i
                end_index = i
            while i < n - 1 and arr[i] <= arr[i + 1]:
                i += 1
            end_index = i
            if end_index != 0:
                troughs.append((start_index, trough_index, end_index))
            start_index = i
        i += 1
        if i == n - 1:
            troughs.append((end_index, i, i))            
    return troughs