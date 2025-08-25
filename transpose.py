def transpose(matrix):
    return [list (row) for row in zip(*matrix)]
M = [[1,2],
    [4,5],
    [3,6]
    ]
transposed_matrix = transpose(M)
print("Transposed Matrix: ")
for row in transposed_matrix:
    print(row)
    
