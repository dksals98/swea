for i in range(10):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(100)]
    count = 0
    for j in range(100):
        state = False
        for k in range(100):
            if not state:
                if table[k][j] == 1:
                    state = True
            if state:
                if table[k][j] == 2:
                    state = False
                    count += 1
    print(f'#{i+1} {count}')
