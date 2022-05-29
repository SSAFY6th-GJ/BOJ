N, M = map(int, input().split())
boards = [list(input()) for _ in range(N)]

def MoveDown(boards):
  for i in range(N):
    for j in range(M):
      if boards[i][j] == 'R':
        if boards[i+1][j] == '.':
          boards[i][j] = '.'
          boards[i+1][j] = 'R'
        elif boards[i+1][j] == 'O':
          return 1
         
      if boards[i][j] == 'B':
        if boards[i+1][j] == '.':
          boards[i][j] = '.'
          boards[i+1][j] = 'B'

        elif boards[i+1][j] == 'O':
          return -1
  return boards

print(MoveDown(boards))