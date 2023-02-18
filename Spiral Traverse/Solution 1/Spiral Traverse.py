def spiralTraverse(array):
    # Write your code here.
    ans = []
    top, bot, left, right = 0, len(array) - 1, 0, len(array[0]) - 1
    n = 0
    while True:
        for i in range(left, right+1):
            ans.append(array[top][i])
            n += 1
        top += 1
        if top > bot:
            break
        
        for i in range(top, bot+1):
            ans.append(array[i][right])
            n += 1
        right -= 1
        if right < left:
            break


        for i in range(right, left-1, -1):
            ans.append(array[bot][i])
            n += 1
        bot -= 1
        if bot < top:
            break


        for i in range(bot, top-1, - 1):
            ans.append(array[i][left])
            n += 1
        left += 1
        if left > right:
            break
    return ans