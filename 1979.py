t = int(input())


def count_one(x, y):
    count = -0
    while (puzzle[x][y]):
        count += 1
        y += 1
        if y > N:
            return count


for t in range(1, t+1):
    N, K = map(int, input().split())
    puzzle = [list(map(int, input().split())) for _ in range(N)]
    word = 0

    for i in range(N):
        w_count = 0
        h_count = 0
        for j in range(N):
            if puzzle[i][j] == 1:
                w_count += 1
            if puzzle[i][j] == 0:
                if w_count == K:
                    word += 1
                w_count = 0
            if puzzle[j][i] == 1:
                h_count += 1
            if puzzle[j][i] == 0:
                if h_count == K:
                    word += 1
                h_count = 0
        if w_count == K:
            word += 1
        if h_count == K:
            word += 1

    print(f'#{t} {word}')
