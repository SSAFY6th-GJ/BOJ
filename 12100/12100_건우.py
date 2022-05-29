from copy import deepcopy
N = int(input())
boards = [list(map(int, input().split())) for _ in range(N)]

def MoveRight(boards):
  for i in range(N):
    for _ in range(len(boards[i])):
      for j in range(N-1, 0, -1):
        if boards[i][j] != 0 and boards[i][j] == boards[i][j-1]:
          boards[i][j] += boards[i][j-1]
          boards[i][j-1] = 0
      zero_count = boards[i].count(0)
      for k in range(zero_count):
        boards[i].remove(0)
      boards[i] = [0] * zero_count + boards[i]
  return boards

def MoveLeft(boards):
  for i in range(N):
    for _ in range(len(boards[i])):
      for j in range(N-1):
        if boards[i][j] != 0 and boards[i][j] == boards[i][j+1]:
          boards[i][j] += boards[i][j+1]
          boards[i][j+1] = 0
      zero_count = boards[i].count(0)
      for k in range(zero_count):
        boards[i].remove(0)
      boards[i] = boards[i] + [0] * zero_count
  return boards
def MoveUp(boards):
  boards_up = [[0]* N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      boards_up[i][j] = boards[N-j-1][i]
  for i in range(N):
    for _ in range(len(boards[i])):
      for j in range(N-1, 0, -1):
        if boards_up[i][j] != 0 and boards_up[i][j] == boards_up[i][j-1]:
          boards_up[i][j] += boards_up[i][j-1]
          boards_up[i][j-1] = 0
      zero_count = boards_up[i].count(0)
      for k in range(zero_count):
        boards_up[i].remove(0)
      boards_up[i] = [0] * zero_count + boards_up[i]
  for i in range(N):
    for j in range(N):
      boards[i][j] = boards_up[j][N-1-i]
  return boards
def MoveDown(boards):
  boards_down = [[0]*N for _ in range(N)]
  for i in range(N):
    for j in range(N):
      boards_down[i][j] = boards[j][N-1-i]
  for i in range(N):
    for _ in range(len(boards[i])):
      for j in range(N-1):
        if boards_down[i][j] != 0 and boards_down[i][j] == boards_down[i][j+1]:
          boards_down[i][j] += boards_down[i][j+1]
          boards_down[i][j+1] = 0
      zero_count = boards_down[i].count(0)
      for k in range(zero_count):
        boards_down[i].remove(0)
      boards_down[i] = boards_down[i] + [0] * zero_count  
  for i in range(N):
    for j in range(N):
      boards[i][j] = boards_down[N-1-j][i]
  return boards
def dfs(boards, cnt):
  global res
  board = deepcopy(boards)
  if cnt == 5:
    for i in range(N):
      for j in range(N):
        res = max(res, board[i][j])
    return
  dfs(MoveUp(board), cnt + 1)
  dfs(MoveDown(board), cnt + 1)
  dfs(MoveLeft(board), cnt + 1)
  dfs(MoveRight(board), cnt + 1)

res = 0
# dfs(boards, 0)
# print(res)

print(MoveDown(boards))

