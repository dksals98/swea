T = int(input())

def check(num1, num2):
    if num2 <= 29:
        return
    if text[num1] == text[num2]:
        check(num2, num2*2-num1)
    else:
        return 0
    return 1
aabaabc

for N in range(1, T+1):
    text = input()
    count = 0
    for i in range(10):
        if text[0] == text[i]:
            if check(0, i) == 0:
                continue;
            for j in range(1, i):
                if check(j, i+j) == 0:
                    break;
            count = i
            break;

    print(count)

