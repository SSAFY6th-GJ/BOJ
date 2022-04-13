from sys import stdin

retter = []
text = stdin.readline().strip()
for i in text:
  retter.append(i)
M = int(stdin.readline())
commands = [list(stdin.readline().split()) for _ in range(M)]
pos = len(retter)
for command in commands:
  # command = stdin.readline().split()
  if command[0] == 'L':
    if pos >= 1:
      pos -= 1
  elif command[0] == 'D':
    if pos < len(retter):
      pos += 1
  elif command[0] == 'B':
    if pos >= 1:
      retter.pop(pos-1)
      pos -= 1
  else:
    retter.insert(pos, command[1])
    pos += 1
res = ''
for ret in retter:
  res += ret
print(res)