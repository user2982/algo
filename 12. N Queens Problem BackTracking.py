ALGORITHM: 
1. Start in the leftmost column. 
2. If all queens are placed, return true. 
3. Try all rows in the current column. For each row, check if the queen can be placed in that position 
without conflicting with already placed queens. 
4. If a safe spot is found, mark this cell and recursively try to place queens in the next columns. 
5. If placing queens in the current configuration leads to a solution, return true. 
6. If placing queens in the current configuration does not lead to a solution, unmark this cell (backtrack) 
and try the next row. 
7. If all rows have been tried and none worked, return false to trigger backtracking to the previous 
column.
-----------------------------------------------------------------------------------------------------------------
PROGRAM:

def is_safe(board, row, col, n): 
    for i in range(col): 
        if board[row][i] == 1: 
            return False 
        
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 

    for i, j in zip(range(row, n, 1), range(col, -1, -1)): 
        if board[i][j] == 1: 
            return False 
    return True 

def solve_n_queens_util(board, col, n): 
    if col >= n: 
        return True 
    for i in range(n): 
        if is_safe(board, i, col, n): 
            board[i][col] = 1 
            if solve_n_queens_util(board, col + 1, n): 
                return True 
            board[i][col] = 0 
    return False 

def solve_n_queens(n): 
    board = [[0] * n for _ in range(n)] 
    if not solve_n_queens_util(board, 0, n): 
        print("Solution does not exist") 
        return 

    print("N Queen problem") 
    print("Solution:") 
    for row in board: 
        print(" ".join(map(str, row))) 

solve_n_queens(4) 
