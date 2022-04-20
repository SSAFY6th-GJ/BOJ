def get_max_gongyak(x,y):
  global max_gongyak
  if x > y:
    k = y
  else:
    k = x
  for i in range(k+1,1,-1):
    if x % i == 0 and y % i ==0:
      max_gongyak = i
      break

A, B = map(int, input().split())
C, D = map(int, input().split())
max_gongyak = 1

get_max_gongyak(B, D)

new_A = A * (D // max_gongyak)
new_B = max_gongyak * (B // max_gongyak * D // max_gongyak)
new_C = C * (B // max_gongyak)
new_D = new_B
# print(max_gongyak)
# print(new_A,new_B,new_C,new_D)

boonja = new_A + new_C
boonmo = new_B

get_max_gongyak(boonja, boonmo)
boonja = boonja // max_gongyak
boonmo = boonmo // max_gongyak
print(boonja, boonmo)