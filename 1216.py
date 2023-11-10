result = []
for _ in range(10):
    N = int(input())
    board = [list(input()) for _ in range(100)]
    max_len = 1
    for i in range(100):
        for j in range(99):
            for k in range(100, j + 2, -1):
                if k - j <= max_len:
                    break
                if board[i][j:k] == board[i][j:k][::-1]:
                    max_len = k - j
                    break

    zip_board = [list(row) for row in zip(*board)]

    for i in range(100):
        for j in range(99):
            for k in range(100, j + 2, -1):
                if k - j <= max_len:
                    break
                if zip_board[i][j:k] == zip_board[i][j:k][::-1]:
                    max_len = k - j
                    break
    result.append(max_len)
for i in range(1, 11):
    print(f'#{i} {result[i-1]}')

