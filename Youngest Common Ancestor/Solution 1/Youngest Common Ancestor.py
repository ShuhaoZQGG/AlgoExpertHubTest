# This is an input class. Do not edit.
class AncestralTree:
    def __init__(self, name):
        self.name = name
        self.ancestor = None




def getYoungestCommonAncestor(topAncestor, descendantOne, descendantTwo):
    if descendantOne == topAncestor or descendantTwo == topAncestor :
        return topAncestor
    
    # Write your code here.
    depthA, depthB = 0, 0
    copyDescedantOne, copyDescedantTwo = descendantOne, descendantTwo
    while copyDescedantOne.ancestor != topAncestor:
        depthA += 1
        copyDescedantOne = copyDescedantOne.ancestor
    while copyDescedantTwo.ancestor != topAncestor:
        depthB += 1
        copyDescedantTwo = copyDescedantTwo.ancestor


    if depthA <= depthB:
        depthA, depthB = depthB, depthA
        descendantOne, descendantTwo = descendantTwo, descendantOne
    
    while depthA > depthB:
        descendantOne = descendantOne.ancestor
        depthA -= 1


    if descendantOne == descendantTwo:
        return descendantOne
    
    while descendantOne.ancestor != descendantTwo.ancestor:
        if descendantOne.ancestor == descendantTwo:
            return descendantTwo
        elif descendantTwo.ancestor == descendantOne: