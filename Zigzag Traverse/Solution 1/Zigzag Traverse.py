def zigzagTraverse(array):
    # Write your code here.
    height = len(array) - 1
    width = len(array[0]) - 1
    output = []
    row, col = 0, 0
    down = True
    while not isOutOfBounds(row, col, height, width):
        output.append(array[row][col])
        if down:
            if col == 0 or row == height:
                down = False
                if row == height:
                    col += 1
                else:
                    row += 1
            else:
                col -= 1
                row += 1
        else:
            if col == width or row == 0:
                down = True
                if col == width:
                    row += 1
                else:
                    col += 1
            else:
                row -= 1
                col += 1
    return output
def isOutOfBounds(row, col, height, width):
    return row < 0 or row > height or col < 0 or col > width