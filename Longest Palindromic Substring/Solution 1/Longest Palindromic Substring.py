def longestPalindromicSubstring(string):
    # Write your code here.
    currentLongest = [0, 1]
    for i in range(1, len(string)):
        odd = getLongestPalindrome(string, i-1, i+1)
        even = getLongestPalindrome(string, i-1, i)
        longest = max(odd, even, key=lambda x:x[1] - x[0])
        currentLongest = max(longest, currentLongest, key = lambda x:x[1]-x[0])
    return string[currentLongest[0] : currentLongest[1]]
    
def getLongestPalindrome(string, leftIdx, rightIdx):
    while leftIdx >= 0 and rightIdx < len(string):
        if string[leftIdx] != string[rightIdx]:
            break
        leftIdx -= 1
        rightIdx += 1
        ## leftIdx + 1 because leftIdx would be < 0 to break the while loop
    return [leftIdx + 1, rightIdx]
    

