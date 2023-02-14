def tournamentWinner(competitions, results):
    # Write your code here.
    hm = {}
    result = ""
    h = 0
    for i in range(len(competitions)):
        if competitions[i][0] not in hm:
            hm[competitions[i][0]] = results[i]
        else:
            hm[competitions[i][0]] += results[i]


        if competitions[i][1] not in hm:
            hm[competitions[i][1]] = 1 - results[i]
        else:
            hm[competitions[i][1]] += 1 - results[i] 
        if hm[competitions[i][0]] > h:
            h = hm[competitions[i][0]] 
            result = competitions[i][0]
        if hm[competitions[i][1]] > h:
            h = hm[competitions[i][1]] 
            result = competitions[i][1]
    return result

