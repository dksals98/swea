max_sums = []
for _ in range(10):
    T = int(input())
    numbers = [list(map(int, input().split())) for _ in range(100)]
    max_sum = 0
    h_sum = 0
    w_sum = 0
    c_sum1 = 0
    c_sum2 = 0
    for j in range(100):
        h_sum = 0
        for k in range(100):
            h_sum += numbers[k][j]
        c_sum1 += numbers[j][j]
        c_sum2 += numbers[99-j][j]
        w_sum = sum(numbers[j])
        max_sum = max(h_sum, w_sum, max_sum)
    max_sum = max(c_sum1, c_sum2, max_sum)
    max_sums.append(max_sum)

for i in range(10):
    print(f'#{i+1} {max_sums[i]}')

#zip함수로 열 튜플 생성 가능