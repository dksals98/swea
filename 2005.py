T = int(input())

for T in range(1, T+1):
    N = int(input())
    line = [[] for _ in range(N+1)]
    for i in range(1, N+1):
        if i == 1:
            line[i].append(1)
        elif i == 2:
            line[i].append(1)
            line[i].append(1)
        else:
            line[i].append(1)
            for j in range(1, i-1):
                line[i].append(line[i-1][j-1] + line[i-1][j])
            line[i].append(1)
    del line[0]
    print(f'#{T}')
    for i in range(N):
        print(*line[i])
