def oneEdit(stringOne, stringTwo):
    # Write your code here.
    diff = abs(len(stringOne) - len(stringTwo))
    if (diff > 1):
        return False


    if diff == 0:
        counter = 0
        for i in range(len(stringOne)):
            if stringOne[i] == stringTwo[i]:
                continue
            counter += 1
        if counter <= 1:
            return True
    else:
        if len(stringOne) < len(stringTwo):
            stringOne, stringTwo = stringTwo, stringOne
        offSet = 0
        for i in range(len(stringTwo)):
            if stringTwo[i] != stringOne[i + offSet]:
                if offSet > 0:
                    return False
                offSet += 1
            if stringTwo[i] != stringOne[i + offSet]:
                return False
        return True
    return False

