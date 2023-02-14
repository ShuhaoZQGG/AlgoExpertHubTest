def classPhotos(redShirtHeights, blueShirtHeights):
    # Write your code here.
    isRedTaller, isBlueTaller = True, True
    redShirtHeights.sort()
    blueShirtHeights.sort()
    for i in range(len(redShirtHeights)):
        if redShirtHeights[i] < blueShirtHeights[i]:
            isRedTaller = False
        elif blueShirtHeights[i] < redShirtHeights[i]:
            isBlueTaller= False
        else:
            isRedTaller, isBlueTaller = False, False
    return isRedTaller or isBlueTaller