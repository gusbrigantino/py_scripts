
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

    box1 = []

    x, y = FindNextEmpty(board)

    IsValid = CheckPlacement(1, board, x, y)

    print(IsValid)

    #for i in range(len(board)):
    #    for j in range(len(board[i])):
    #        print(str(j) + ": " + str(board[i][j]))


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
