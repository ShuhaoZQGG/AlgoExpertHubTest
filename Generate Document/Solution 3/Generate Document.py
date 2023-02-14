def generateDocument(characters, document):
    # Write your code here.
    # print(sorted(characters.split(" ")).join())
    hm = {}
    for i in range(len(characters)):
        c = characters[i]
        if c not in hm:
            hm[c] = 1
        else:
            hm[c] += 1
    
    length = len(document)
    for i in range(length):
        c = document[i]
        if c == "":
            continue
        elif c not in hm:
            return False
        else:
            if hm[c] < 1:
                return False
            else:
                hm[c] -= 1
    return True

