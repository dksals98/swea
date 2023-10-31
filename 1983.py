t = int(input())

def tochar(num):
    if num <= 1:
        return 'A+'
    elif 1 < num <= 2:
        return 'A0'
    elif 2 < num <= 3:
        return 'A-'
    elif 3 < num <= 4:
        return 'B+'
    elif 4 < num <= 5:
        return 'B0'
    elif 5 < num <= 6:
        return 'B-'
    elif 6 < num <= 7:
        return 'C+'
    elif 7 < num <= 8:
        return 'C0'
    elif 8 < num <= 9:
        return 'C-'
    elif 9 < num <= 10:
        return 'D0'


for i in range(1, t+1):
    N, K = map(int, input().split())
    scores = [[0]*5 for _ in range(N)]
    credit = [0]*N
    for j in range(N):
        scores[j][0] = j+1
        scores[j][1], scores[j][2], scores[j][3] = map(int, input().split())
        credit[j] = scores[j][1]*0.35 + scores[j][2]*0.45 + scores[j][3]*0.2
        scores[j][4] = credit[j]
    credit.sort(reverse=True)
    percent = (credit.index(scores[K-1][4])+1)*10 / N
    print(f'#{i} {tochar(percent)}')
