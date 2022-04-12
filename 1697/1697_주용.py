from collections import deque
def bfs(x):
    # cnt 로 해주는 방법은 왜 안되는거지
    # cnt = 0
    queue = deque()
    queue.append(x)
    while queue:
        a = queue.popleft()
        if a == K:
            print(visited[a])
            # print(cnt)
            break
        move = [a-1, a+1, a*2]
        for i in move:
            if 0 <= i < 100001 and visited[i] == 0:
                visited[i] = visited[a] + 1
                queue.append(i)
        # cnt += 1

N, K = map(int, input().split())
visited = [0] * 100001
bfs(N)
