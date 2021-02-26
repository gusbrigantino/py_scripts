
def main():  
    board = [
    [1, 4, 7, 0, 0, 0, 0, 0, 3],
    [2, 5, 0, 0, 0, 1, 0, 0, 0],
    [3, 0, 9, 0, 0, 0, 0, 0, 0],
    [0, 8, 0, 0, 2, 0, 0, 0, 4],
    [0, 0, 0, 4, 1, 0, 0, 2, 0],
    [9, 0, 0, 0, 0, 0, 6, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 9],
    [4, 0, 0, 0, 0, 2, 0, 0, 0],
    [0, 0, 1, 0, 0, 8, 0, 0, 7]
    ]

    for x in board:
        print(x)
    
    x, y = FindNextEmpty(board)

    for val in range(1, 10):
        if CheckPlacement(val, board, x, y):
            board[x][y] = val
            

    print()
    for x in board:
        print(x)


def SolveSudoku(board):
    x, y = FindNextEmpty(board)

    if not x and not y:
        print("not")
        return True
    
    for val in range(1, 10):      #values
        if CheckPlacement(val, board, x, y):
            board[x][y] = val

            if SolveSudoku(board):
                return True
            
            board[x][y] = 0

    return False



def FindNextEmpty(board):
    for x in range(len(board)):
        for y in range(len(board[x])):
            if board[x][y] == 0:
                return x, y

def CheckPlacement(newNum, board, x, y):
    IsValid = True
    #check row
    for val in board[x]:
        if val == newNum:
            IsValid = False
            return IsValid

    #check column
    for col in range(len(board)):
        if(board[col][y] == newNum):
            IsValid = False
            return IsValid

    #check box
    xRange, yRange = GetBoxRanges(x, y)

    for i in xRange:
        for j in yRange:
            if board[i][j] == newNum:
                IsValid = False
                return IsValid

    return IsValid


def GetBoxRanges(x, y):
    if x in range(0, 3) and y in range(0, 3):
        return range(0, 3), range(0, 3)

    elif x in range(0, 3) and y in range(3, 6):
        return range(0, 3), range(3, 6)

    elif x in range(0, 3) and y in range(6, 9):
        return range(0, 3), range(6, 9)

    elif x in range(3, 6) and y in range(0, 3):
        return range(3, 6), range(0, 3)

    elif x in range(3, 6) and y in range(3, 6):
        return range(3, 6), range(3, 6)

    elif x in range(3, 6) and y in range(6, 9):
        return range(3, 6), range(6, 9)

    elif x in range(6, 9) and y in range(0, 3):
        return range(6, 9), range(0, 3)

    elif x in range(6, 9) and y in range(3, 6):
        return range(6, 9), range(3, 6)

    elif x in range(6, 9) and y in range(6, 9):
        return range(6, 9), range(6, 9)
    
    else:
        return -1, -1




if __name__ == "__main__":
    main()
