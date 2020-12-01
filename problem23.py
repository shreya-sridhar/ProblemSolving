def dfs(grid, row, col, index, word):
    if index == len(word):
        return True
    elif row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1:
        return False
    elif grid[row][col] != word[index]:
        return False      
    else:
        temp = grid[row][col]
        grid[row][col] = 'X'
        res = dfs(grid, row+1,col, index+1,word) or dfs(grid, row,col+1, index+1,word) or dfs(grid, row-1,col, index+1,word) or dfs(grid, row ,col-1, index+1,word)
        grid[row][col] = temp
        return res

def exist(grid, word):
    index = 0
    for row in range(len(grid)):
        for col in range(len(grid[0])):
            is_visited = []
            if dfs(grid, row, col, index, word):
                return True
    return False


board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
word = "CESEEE"
print(exist(board,word))

