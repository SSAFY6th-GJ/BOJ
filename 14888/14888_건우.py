from collections import deque


N = int(input())
numbers = list(map(int, input().split()))
plus, minus, multi, divide = map(int, input().split())

max_answer = -1000000000
min_answer = 1000000000

def make_soosik(num, res):
    global max_answer, min_answer
    if num == N:
        max_answer = max(res, max_answer)
        min_answer = min(res, min_answer)
        return

    global plus, minus, multi, divide
    if plus > 0:
        plus -= 1
        make_soosik(num + 1, res + numbers[num])
        plus += 1
    if minus > 0:
        minus -= 1
        make_soosik(num + 1, res - numbers[num])
        minus += 1
    if multi > 0:
        multi -= 1
        make_soosik(num + 1 , res * numbers[num])
        multi += 1
    if divide > 0:
        if res < 0:
            divide -= 1
            make_soosik(num + 1, -(-res // numbers[num]))
            divide += 1
        else:
            divide -= 1
            make_soosik(num + 1, res // numbers[num])
            divide += 1
make_soosik(1, numbers[0])
print(max_answer, min_answer)

# def test(num, res):
#     global max_answer, min_answer
#     if num == N:
#         max_answer = max(res, max_answer)
#         min_answer = min(res, min_answer)
#         return
#     if num == 1:
#         test(num + 1, res - numbers[num])
#     if num == 2: 
#         test(num + 1, res // numbers[num])
#     if num == 3:
#         test(num + 1, res + numbers[num])
#         max_answer = max(res, max_answer)
#         return


# test(1, numbers[0])
# print(max_answer, min_answer)