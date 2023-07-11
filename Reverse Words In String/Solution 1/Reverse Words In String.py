def reverseWordsInString(string):
    # Write your code here.
    input = []
    word = ""
    for i in range(len(string)):
        if string[i] == " ":
            input.append(word)
            word = ""
        else:
            word += string[i]
    input.append(word)
    output = ""
    for i in range(len(input)-1, -1, -1):
        output += input[i] + " "
    return output[:-1]