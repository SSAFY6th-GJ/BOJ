# 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸
# 인접한 칸 중에서 비어있는 칸이 가장 많은 칸
# 행의 번호가 작은칸 -> 열의 번호가 작은 칸

N = int(input())
base = [[]for _ in range(N**2+1)]
like = [list(map(int, input().split())) for _ in range(N**2)]