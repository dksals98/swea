T = int(input())


for i in range(1, T+1):
    N = int(input())
    farm = [list(map(int, input())) for _ in range(N)]
    top = N
    center = N // 2
    bottom = 0
    result = 0
    for j in range(1, center + 1):
        bottom += 1
        top -= 1
        for k in range(bottom, top):
            result += farm[center-j][k] + farm[center+j][k]
    for j in range(N):
        result += farm[center][j]

    print(f'#{i} {result}')
