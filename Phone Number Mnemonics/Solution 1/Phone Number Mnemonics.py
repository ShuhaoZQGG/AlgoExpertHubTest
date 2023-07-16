def phoneNumberMnemonics(phoneNumber):
    # Write your code here.
    map = {
        "1": ["1"],
        "2": ["a", "b", "c"],
        "3": ["d", "e", "f"],
        "4": ["g", "h", "i"],
        "5": ["j", "k", "l"],
        "6": ["m", "n", "o"],
        "7": ["p", "q", "r", "s"],
        "8": ["t", "u", "v"],
        "9": ["w", "x", "y", "z"],
        "0": ["0"]
    }


    output = []
    recursion(phoneNumber, "", output, map, 0)
    return output


def recursion(phoneNumber, currentCombination, mnemonic, map, index):
   if index == len(phoneNumber):
       mnemonic.append(currentCombination)
       return mnemonic
    
   for j in range(len(map[phoneNumber[index]])):
       transformation = map[phoneNumber[index]][j]
       recursion(phoneNumber, currentCombination + transformation, mnemonic, map, index+1)