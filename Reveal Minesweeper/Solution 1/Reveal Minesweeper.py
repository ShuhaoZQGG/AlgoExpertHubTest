def revealMinesweeper(board, row, col):
    # Write your code here.
    if board[row][col] == "M":
        board[row][col] = "X"
        return board
    height = len(board)
    width = len(board[0])
    dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
    q = [(row, col)]
    while q:
        numberOfMines = 0
        spot = q.pop()
        r, c = spot
        for dir in dirs:
            x, y = dir
            ROW = r + x
            COL = c + y
            if ROW >= 0 and ROW < height and COL >= 0 and COL < width:
                if board[ROW][COL] == "M":
                    numberOfMines += 1
        if numberOfMines == 0:
            for dir in dirs:
                x, y = dir
                ROW = r + x
                COL = c + y
                if ROW >= 0 and ROW < height and COL >= 0 and COL < width:
                    if board[ROW][COL] == "H":
                        q.append((ROW, COL))
        board[r][c] = str(numberOfMines)
    return board