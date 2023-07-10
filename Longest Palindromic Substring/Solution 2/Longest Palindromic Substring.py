def longestPalindromicSubstring(string):
    # Write your code here.
    longest = [0, 1]
    for i in range(len(string)):
        odd = getPalindrome(string, i-1, i+1)
        even = getPalindrome(string, i-1, i)
        # key = lambda x : x[1] - x[0]
        # x[1] - x[0] is the length of the palindrome
        # get the max between odd and even based on length of the palindrome
        currentLongest = max(odd, even, key = lambda x: x[1] - x[0])
        longest = max(longest, currentLongest, key = lambda x: x[1] - x[0])
    return string[longest[0] : longest[1]]


def getPalindrome(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] == string[rightIdx]:
            leftIdx -= 1
            rightIdx += 1
        else:
            break
    return [leftIdx + 1, rightIdx]