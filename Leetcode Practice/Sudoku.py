import math
sudoku = [
    [3,0,0,0,0,0,0,0,9],
    [0,7,0,0,4,0,0,3,0],
    [0,0,6,1,0,3,5,0,0],
    [0,0,7,0,3,0,8,0,0],
    [0,8,0,2,0,4,0,1,0],
    [0,0,5,0,7,0,6,0,0],
    [0,0,2,3,0,7,4,0,0],
    [0,1,0,0,6,0,0,2,0],
    [8,0,0,0,0,0,0,0,7]
]
def check_position(row, col, element):
    grid = int(math.sqrt(len(sudoku[0])))

    #Check row
    for i in range(len(sudoku[0])):
        if sudoku[row][i] == element:
            return False
    
    #Check column
    for index in range(len(sudoku[0])):
        if sudoku[index][col] == element:
            return False
    
    #Check Grid
    grid_row = row - row % grid
    grid_col = col - col % grid
    for row in range(grid_row, grid_row + grid):
        for col in range(grid_col, grid_col + grid):
            if sudoku[row][col] == element:
                return False

    return True

def solve(row, col):
    if row == len(sudoku[0])-1 and col == len(sudoku[0]):
        return True
    if col == len(sudoku[0]):
        row += 1
        col = 0
    if sudoku[row][col] > 0:
        return solve(row, col+1)
    for num in range(1, len(sudoku[0])+1):
        if check_position(row, col, num):
            sudoku[row][col] = num
            if solve(row, col+1):
                return True
        sudoku[row][col] = 0
    return False
        

def solve_sudoku():
    solve(0, 0)
solve_sudoku()
print(f"Solved : \n{sudoku}")