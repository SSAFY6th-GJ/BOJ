T = int(input())
for t in range(T):
  x1, y1, r1, x2, y2, r2 = map(int, input().split())
  distance = ((x1 - x2) ** 2 +(y1- y2)**2)**(1/2)
  
  if distance == 0 and r1 == r2:
    print(-1)
  elif distance == 0  and r1 != r2:
    print(0)
  elif distance != 0: 
    if r1 + r2 == distance or abs(r2-r1) == distance:
      print(1)
    elif abs(r2-r1) < distance < r1+r2:
      print(2)
    else:
      print(0)