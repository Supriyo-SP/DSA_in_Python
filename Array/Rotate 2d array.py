matrix = [[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

r = len(matrix)
c = len(matrix[0])

# Same size as matrix: r rows and c columns
result = [[0] * c for _ in range(r)]

# Rotate matrix 90 degrees clockwise into result
for i in range(r):
    for j in range(c):
        result[j][r - 1 - i] = matrix[i][j]

print(result)