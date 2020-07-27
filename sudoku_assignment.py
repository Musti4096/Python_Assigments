sudoku = [
    [0, 0, 0, 0, 6, 4, 0, 0, 0],
    [7, 0, 0, 0, 0, 0, 3, 9, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 5, 0, 2, 0, 6, 0],
    [0, 8, 0, 4, 0, 0, 0, 0, 0],
    [3, 5, 0, 6, 0, 0, 0, 7, 0],
    [0, 0, 2, 0, 0, 0, 1, 0, 3],
    [0, 0, 1, 0, 5, 9, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0]
]
sudoku_new = []
for i in sudoku:
    row = []
    for j in range(len(i)):
        if j == 3 or j == 6:
            row.append("|")
            row.append(i[j])
        else:
            row.append(i[j])
    sudoku_new.append(row)


for i in range(len(sudoku_new)):
    #print(sudoku[i])
    if i == 0:
        print("- - - - - - - - - - - ")
        a = 0
        for j in sudoku_new[i]:
            if a == 10:
                print(j,)
            else:
                print(j, end=" ")
            a += 1
    elif i == 2 or i == 5 or i == 8:
        for j in sudoku_new[i]:
            a = 0
        for j in sudoku_new[i]:
            if a == 10:
                print(j,)
            else:
                print(j, end=" ")
            a += 1
        print("- - - - - - - - - - - ")
    else:
        for j in sudoku_new[i]:
            a = 0
        for j in sudoku_new[i]:
            if a == 10:
                print(j,)
            else:
                print(j, end=" ")
            a += 1
