from collections import deque

T = int(input())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def check(x, y):
    for i in range(4):
        nx = x
        ny = y
        while 0 < nx <= N and 0 < ny <= N:
            nx += dx[i]
            ny += dy[i]
            if frame[nx][ny]:
                return False
        return True


def bfs():
    visited[x][y] = 1
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    while deque:
        a, b = deque.popleft()
        if visited[x][y] == 0:
            for i in range(4):


for i in range(1, T+1):
    N = int(input())
    frame = [[map(int, input().split())] for _ in range(X)]
    visited = [[0] * X for _ in range(X)][]
    cores = []
    queue = deque()
    count = 0

    for j in range(1, N-1):
        for k in range(1, N-1):
            if frame[j][k] == 1:
                queue.append((j, k))

    bfs()
