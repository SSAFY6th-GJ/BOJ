N = int(input())
M = int(input())
buttons = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
if M >0:
  buttons_broken = list(map(int, input().split()))
else:
  buttons_broken = []
for button_broken in buttons_broken:
  for button in buttons:
    if button_broken == button:
      buttons.remove(button_broken)
      break
buttons = list(map(str, buttons))
# print(buttons)
check = [True] * 1000000
def checking(a):
  for button in a:
    if button not in buttons:
      check[i] = False
      return

min_cnt = 100000
min_value = 0
for i in range(1000000):
  a = str(i)
  checking(a)
for j in range(1000000):
  if check[j]:
    # min_cnt = min(min_cnt,abs(N - j))
    if min_cnt > abs(N-j):
      min_cnt = abs(N-j)
      min_value = j
min_cnt += len(str(min_value))
answer = abs(N - 100)
if answer > min_cnt:
  print(min_cnt)
else:
  print(answer)