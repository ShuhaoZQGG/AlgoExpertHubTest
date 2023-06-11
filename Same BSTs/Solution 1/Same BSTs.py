def sameBsts(arrayOne, arrayTwo):
    # Write your code here.
    if not arrayOne and not arrayTwo:
        return True
    if len(arrayOne) != len(arrayTwo):
        return False
    if arrayOne[0] != arrayTwo[0]:
        return False
    firstIntegerArrayOne = arrayOne[0]
    firstIntegerArrayTwo = arrayTwo[0]
    del arrayOne[0]
    del arrayTwo[0]
    leftSubTreeArrayOne = list(filter(lambda x: x < firstIntegerArrayOne, arrayOne))
    rightSubTreeArrayOne = list(filter(lambda x: x >= firstIntegerArrayOne, arrayOne))
    leftSubTreeArrayTwo = list(filter(lambda x: x < firstIntegerArrayTwo, arrayTwo))
    rightSubTreeArrayTwo = list(filter(lambda x: x >= firstIntegerArrayTwo, arrayTwo))
    return sameBsts(leftSubTreeArrayOne, leftSubTreeArrayTwo) and sameBsts(rightSubTreeArrayOne, rightSubTreeArrayTwo)