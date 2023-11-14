T = int(input())
result = []


def dfs(num, count, visited_copy):
    global max_count
    visited_copy[num] = True
    if max_count < count:
        max_count = count
    for i in table[num]:
        if not visited_copy[i]:
            dfs(i, count + 1, visited_copy[:])


for i in range(1, T + 1):
    n, m = map(int, input().split())
    table = [[] for _ in range(n + 1)]

    for _ in range(m):
        a, b = map(int, input().split())
        table[a].append(b)
        table[b].append(a)

    visited = [False] * (n+1)
    max_count = 1

    for j in range(1, n+1):
        dfs(j, 1, visited[:])

    result.append(max_count)

for i in range(T):
    print(f'#{i+1} {result[i]}')