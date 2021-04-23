from collections import deque

def wordFind(board,word,row,col):
    index = 0
    q = deque()
    is_visited = []
    q.append([row,col])
    is_visited.append([row,col])
    while q:
        popped_ele = q.pop()
        for [neighbor_row,neighbor_col] in [[popped_ele[0]-1,popped_ele[1]],[popped_ele[0],popped_ele[1]+1],[popped_ele[0],popped_ele[1]-1],[popped_ele[0]+1,popped_ele[1]]]:
            if word[index+1] == board[neighbor_row][neighbor_col] and [neighbor_row,neighbor_col] not in is_visited :
                index += 1
                q.append([neighbor_row,neighbor_co])
    if index == len(word)-1:
        return [row,col]
    
def searchBoard(board,word):   
    for row in len(board):
        for col in len(board[0]):
            if board[row][col] == word[0]:
                wordFind(board,word,row,col)


board1 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word1 = "ABCCED"
board2 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word2 = "SEE"
board3 = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word3 = "ABCB"

print(wordFind(board1,word1))
print(wordFind(board2,word2))
print(wordFind(board3,word3))

