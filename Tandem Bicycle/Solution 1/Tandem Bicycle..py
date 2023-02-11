def tandemBicycle(redShirtSpeeds, blueShirtSpeeds, fastest):
    # Write your code here.
    ans = 0
    if fastest == True:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort(reverse=True)
        for i in range(len(redShirtSpeeds)):
            ans += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    else:
        redShirtSpeeds.sort()
        blueShirtSpeeds.sort()
        for i in range(len(redShirtSpeeds)):
            ans += max(redShirtSpeeds[i], blueShirtSpeeds[i])
    return ans



