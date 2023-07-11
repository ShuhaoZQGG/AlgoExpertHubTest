def groupAnagrams(words):
    # Write your code here.
    map = {}
    output = []
    for word in words:
        sortedWord = ''.join(sorted(word))
        if sortedWord not in map:
            map[sortedWord] = [word]
        else:
            map[sortedWord].append(word)


    for k, v in map.items():
        output.append(v)
    return output

