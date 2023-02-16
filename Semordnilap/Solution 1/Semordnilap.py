def semordnilap(words):
    # Write your code here.
    hm = {}
    for i in range(len(words)):
        sortedW = "".join(sorted(words[i]))
        if sortedW not in hm:
            hm[sortedW] = [i, -1]
        else:
            index1, index2 = hm[sortedW]
            hm[sortedW] = [index1, i]
    ans = []
    for k, v in hm.items():
        index1, index2 = v
        if index2 != -1:
            ans.append([words[index1], words[index2]])
    return ans