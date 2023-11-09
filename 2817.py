t = int(input())


def dfs(num, sum):
    global count
    if num >= N:
        return
    plus_sum = sum + seq[num]
    dfs(num + 1, sum)
    if plus_sum < K:
        dfs(num+1, plus_sum)
    elif plus_sum == K:
        count += 1
        return
    else:
        return


for i in range(1, t+1):
    N, K = map(int, input().split())
    count = 0
    seq = list(map(int, input().split()))
    dfs(0, 0)
    print(f'#{i} {count}')
