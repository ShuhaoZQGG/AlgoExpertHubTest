def iterativeInOrderTraversal(tree, callback):
    # Write your code here.
    map = {}
    q = [tree]
    while q:
        node = q[-1]
        if node.value not in map:
            map[node.value] = { 'left': False, 'right': False, 'callback': False }
        if map[node.value]:
            if map[node.value]['right'] == True:
                q.pop()
        if node.left and map[node.value]['left'] == False:
            q.append(node.left)
            map[node.value]['left'] = True
        else:
            map[node.value]['left'] == True
            if map[node.value]['callback'] == False:
                callback(node)
                map[node.value]['callback'] = True
            if node.right and map[node.value]['right'] == False:
                q.append(node.right)
                map[node.value]['right'] = True
            else:
                map[node.value]['right'] = True


            