def rotate(matrix):
    n = len(matrix)
    for i in range(n//2 + n%2):
        for j in range (n//2):
             temp = matrix[i][j]
             matrix[i][j] = matrix[j][n-1-i]
             matrix[j][n-1-i] = matrix[n-1-i][n-1-j]
             matrix[n-1-i][n-1-j] = matrix[n-1-j][i]
             matrix[n-1-j][i] = temp
    return matrix

print(rotate([[1,2,3],[4,5,6],[7,8,9]]))


