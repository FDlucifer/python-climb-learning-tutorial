matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

for row in matrix:
    for element in row:
        if element == 11:
            print("found 11. quitting search.")
            break
    else:
        continue
    break

