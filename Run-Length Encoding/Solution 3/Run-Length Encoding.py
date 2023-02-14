def runLengthEncoding(string):
    result = ''
    count = 1
    for i in range(len(string)):
        char = string[i]
        if i < len(string) - 1 and string[i + 1] == char:
            count += 1
        else:
            if count != 9:
                times = count // 9
                remain = count % 9
                c9 = '9' + char
                result += (times * c9 + (str(remain) + char))
            else:
                times = count // 9
                c9 = '9' + char
                result += times * c9 
            count = 1
    return result