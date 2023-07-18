def revealMinesweeper(board, row, column):
    # Write your code here.
    def bfs(row, col):
        numberOfMines = 0
        height = len(board)
        width = len(board[0])
        if board[row][col] == "M":
            board[row][col] = "X"
            return
        dirs = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]
        
        for dir in dirs:
            x, y = dir
            ROW, COL = x + row, y + col
            if ROW >= 0 and ROW < height and COL >= 0 and COL < width:
                if board[ROW][COL] == "M":
                    numberOfMines += 1
        board[row][col] = str(numberOfMines)
        if board[row][col] == "0":
            for dir in dirs:
                x, y = dir
                ROW, COL = x + row, y + col
                if ROW >= 0 and ROW < height and COL >= 0 and COL < width:
                    if board[ROW][COL] == "H":
                        bfs(ROW, COL)


    bfs(row, column)
    return board

