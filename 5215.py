T = int(input())


def dfs(i, cal, taste):
    global max_taste
    max_taste = max(max_taste, taste)
    if i == N:
        return

    plus_cal = cal + ingredients[i][1]
    plus_taste = taste + ingredients[i][0]
    dfs(i + 1, cal, taste)

    if plus_cal > L:
        return

    dfs(i + 1, plus_cal, plus_taste)


for i in range(1, T + 1):
    N, L = map(int, input().split())
    ingredients = [list(map(int, input().split())) for _ in range(N)]
    max_taste = 0
    dfs(0, 0, 0)
    print(f'#{i} {max_taste}')