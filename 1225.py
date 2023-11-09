for i in range(10):
    N = int(input())
    result = []
    password = list(map(int, input().split()))
    min_val = min(password)
    cycle = min_val // 15
    for j in range(8):
        password[j] = password[j] - cycle * 15

    num = 0
    val = 1
    while True:
        temp = password[num] - val
        if temp <= 0:
            password.append(0)
            result.append(list(password[num+1:num+10]))
            break;
        password.append(temp)
        num += 1
        val += 1
        if val == 6:
            val = 1

print(result)
