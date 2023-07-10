def validIPAddresses(string):
    # Write your code here.
    output = []
    for i in range(1, min(len(string), 4)):
        ip = ['', '', '', '']
        ip[0] = string[:i]
        if not isValid(ip[0]):
            continue


        for j in range(i + 1, min(len(string), i + 4)):
            ip[1] = string[i: j]
            if not isValid(ip[1]):
                continue


            for k in range(j + 1, min(len(string), i + j + 4)):
                ip[2] = string[j:k]
                ip[3] = string[k:]
                if not isValid(ip[2]) or not isValid(ip[3]):
                    continue
                output.append('.'.join(ip))
    return output


def isValid(string):
    num = int(string)
    if num < 0 or num > 255:
        return False
    return len(str(num)) == len(string)