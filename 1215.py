counts = []

for i in range(1, 11):
    w_len = int(input())
    board = [input() for _ in range(8)]
    count = 0
    for j in range(8):
        for k in range(9-w_len):
            if board[j][k:k+w_len] == board[j][k:k+w_len][::-1]:
                count += 1
            temp = []
            for l in range(k, k+w_len):
                temp += board[l][j]
            if temp == temp[::-1]:
                count += 1
    counts.append(count)

for i in range(10):
    print(f'#{i+1} {counts[i]}')
