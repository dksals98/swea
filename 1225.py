result = []
for i in range(10):
    N = int(input())
    password = list(map(int, input().split()))
    min_val = min(password)
    cycle = min_val // 15
    for j in range(8):
        password[j] = password[j] - cycle * 15
    for num in password:
        if num == 0:
            for j in range(8):
                password[j] = password[j] + 15
            break

    num = 0
    val = 1
    while True:
        temp = password[num] - val
        if temp <= 0:
            password.append(0)
            result.append(password[num+1:num+10])
            break
        password.append(temp)
        num += 1
        val += 1
        if val == 6:
            val = 1

for i in range(10):
    print(f'#{i+1}', end=' ')
    for j in range(8):
        print(result[i][j], end=' ')
    print('')
