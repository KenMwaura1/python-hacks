matrix = [(7, 6, 8), (9, 10, 11), (12, 13, 14), (15, 16, 17)]
for row in matrix:
    print(row)
    print('\n')
    t_matrix = zip(*matrix)
    for row1 in t_matrix:
        print(row1)
