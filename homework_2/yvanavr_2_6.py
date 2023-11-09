# A function to calculate the total perimeter of all the islands
def perim(arr):
    perimeter = 0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == 'X':
                if 0 < i < (len(arr) - 1):
                    if arr[i-1][j] == "O":
                        perimeter += 1
                    if arr[i+1][j] == "O":
                        perimeter += 1
                if i == 0:
                    perimeter += 1
                    if arr[i + 1][j] == "O":
                        perimeter += 1
                if i == len(arr) - 1:
                    perimeter += 1
                    if arr[i - 1][j] == "O":
                        perimeter += 1

                if 0 < j < (len(arr[0])-1):
                    if arr[i][j - 1] == "O":
                        perimeter += 1
                    if arr[i][j + 1] == "O":
                        perimeter += 1
                if j == 0:
                    perimeter += 1
                    if arr[i][j + 1] == "O":
                        perimeter += 1
                if j == len(arr[0]) - 1:
                    perimeter += 1
                    if arr[i][j - 1] == "O":
                        perimeter += 1
    return perimeter


a = ['XOOO', 'XOXO', 'XOXO', 'OOXX', 'OOOO']

print(perim(a))
