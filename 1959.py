T = int(input())

for i in range(1, T+1):
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    count = abs(M - N) + 1
    if M >= N:
        big = B
        small = A
        small_len = N
    else:
        big = A
        small = B
        small_len = M
    max_sum = 0
    sum = 0

    for k in range(count):
        for j in range(small_len):
            sum += big[j + k] * small[j]
        max_sum = max(sum, max_sum)
        sum = 0

    print(f'#{i} {max_sum}')
