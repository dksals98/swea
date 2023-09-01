t = int(input())
result = [0] * t

def checking(B):
    for i in range(9):
        row_nums = [0] * 10
        col_nums = [0] * 10
        for j in range(9):
            if row_nums[B[i][j]] == 1:
                return 0
            if col_nums[B[j][i]] == 1:
                return 0
            row_nums[B[i][j]] = 1
            col_nums[B[j][i]] = 1

    for h in range(3):
        for i in range(3):
            square_nums = [0] * 10
            for j in range(3):
                for k in range(3):
                    if square_nums[B[3*h+j][3*i+k]] == 1:
                        return 0
                    square_nums[B[3*h+j][3*i+k]] = 1

    return 1


for i in range(t):
    board = [list(map(int, input().split())) for _ in range(9)]

    if checking(board) == 1:
        result[i] = 1

for i in range(t):
    print(f'#{i+1} {result[i]}')


