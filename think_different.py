from collections import deque
dxy = [[0,1],[-1,0],[0,-1],[1,0]]
T=int(input())

for test_case in range(1,1+T):
    N,M = map(int,input().split())
    matrix = [list(input().strip()) for _ in range(N)]
    dist = [[-1]*M for _ in range(N)]
    Queue = deque()
    for i in range(N):
        for j in range(M):
            if matrix[i][j] == 'W':
                Queue.append((i,j,0))
                dist[i][j] = 0

    while Queue :
        cx, cy, dists = Queue.popleft()

        for dx, dy in dxy:
            nx, ny = cx + dx, cy + dy
            if 0 <= nx < N and 0 <= ny < M :
                if dist[nx][ny] == -1:
                    dist[nx][ny] = dists+1
                    Queue.append((nx, ny, dists + 1))
    p =0
    for i in range(N):
        p += sum(dist[i])

    print(f"#{test_case} {p}")