N, K = map(int, input().split())
use = list(map(int, input().split()))
plug = [0] * N
# 2 3은 계속 꽂혀 있고 3이 꽂힌 자리 대신에 1이 꽂히고 2나 1자리에 7이 꽂히니까 답은 2
# 1 2 2 2 3 3 7
set_use = set(use)
# for x in range(len(use)):
#     if use[x] not in plug:
#         for x in range(len(plug)):
#             if plug[x] == 0:
#                 plug[x] = use[x]
print(len(set_use) - N)