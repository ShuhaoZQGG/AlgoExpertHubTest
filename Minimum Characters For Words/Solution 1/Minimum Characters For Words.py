def minimumCharactersForWords(words):
    # Write your code here.
    map = {}
    output = []
    for word in words:
        frequency = {}
        for i in range(len(word)):
            c = word[i]
            if c not in map:
                map[c] = 1
            if c not in frequency:
                frequency[c] = 1
            else:
                frequency[c] += 1
                if frequency[c] > map[c]:
                    map[c] = frequency[c]
    for k, v in map.items():
        for i in range(v):
            output.append(k)
    return output

