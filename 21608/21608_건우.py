# def condition():

  

di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
N = int(input())
students = [list(map(int, input().split())) for _ in range(N**2)]
table = [[0] * N for _ in range(N)]
score = 0
# table_score = [[0] * N for _ in range(N)]
for student in students:
  print(table)
  student_num = student[0]
  print(student_num)
  like_student = student[1:5]
  table_score = [[0] * N for _ in range(N)]
  max_1 = 0
  max_2 = 0

  # print(table_score)
  for i in range(N):
    for j in range(N):
      for d in range(4):
        new_i = i + di[d]
        new_j = j + dj[d]
        if 0 <= new_i < N and 0 <= new_j < N and table[i][j] == 0:
          if table[new_i][new_j] in like_student:
            table_score[i][j] += 1

  for i in range(N):
    for j in range(N):
      if table_score[i][j] > max_1:
        max_1 = table_score[i][j]
  for i in range(N):
    for j in range(N):
      if table_score[i][j] == max_1:
        for d in range(4):
          new_i = i + di[d]
          new_j = j + dj[d]
          if 0 <= new_i < N and 0 <= new_j < N and table[new_i][new_j] == 0:
            table_score[i][j] += 1
  print(table_score)
  for i in range(N):
    for j in range(N):
      if table_score[i][j] > max_2:
        max_2 = table_score[i][j]
  print(max_2)
  breaking = False
  for i in range(N):
    for j in range(N):
      if table_score[i][j] == max_2:
        table[i][j] = student_num
        breaking = True
        break
    if breaking:
      break
  print('************************')
  
  for i in range(N):
    for j in range(N):
      like_student_cnt = 0
      for d in range(4):
        new_i = i + di[d]
        new_j = j + dj[d]
        if 0 <= new_i < N and 0 <= new_j < N:
          if table[new_i][new_j] in like_student:
            like_student_cnt += 1
      if like_student_cnt == 1:
        score += 1
      elif like_student_cnt == 2:
        score += 10
      elif like_student_cnt == 3:
        score += 100
      elif like_student_cnt == 4:
        score += 1000

print(score)