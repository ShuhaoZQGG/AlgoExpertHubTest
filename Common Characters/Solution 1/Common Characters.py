def commonCharacters(strings):
    # Write your code here.
    map = {}
    output = []
    for string in strings:
        visited = set()
        for c in string:
            if c not in visited:
                visited.add(c)
                if c in map:
                    map[c] += 1
                else:
                    map[c] = 1


    for k, v in map.items():
        if v == len(strings):
            output.append(k)
    return output

