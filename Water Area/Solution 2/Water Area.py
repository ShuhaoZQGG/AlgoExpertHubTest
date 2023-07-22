from itertools import accumulate
def waterArea(heights):
    # Write your code here.
    left_max = list(accumulate(heights, max))


    right_max = list(reversed(list(accumulate(reversed(heights), max))))


    depths = [min(lm, rm) for lm, rm in zip(left_max, right_max)]


    water = sum(depths) - sum(heights)


    return water

