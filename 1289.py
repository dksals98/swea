T = int(input())
count = [0] * (T + 1)

for i in range(1, T+1):
    code = list(map(int, input()))
    state = 1
    count[0] = 0

    for j in code:
        if state == j:
            count[0] += 1
            state = abs(j-1)
    count[i] = count[0]

for j in range(1, T+1):
    print(f'#{j} {count[j]}')
