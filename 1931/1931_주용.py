N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
arr.sort(key=lambda x:(x[1] ,x[0]))
# 끝나는 시간으로 정렬해야 된다. 시작하는 시간으로 정렬하면 처음에 시작하고 제일 마지막에 끝날 수도 있으니
# 끝나는 시간으로 정렬한다음에 처음에 시작하는건 무조건 한다고 치고 끝나는 시간이랑 그 다음 시작하는 시간 비교하기
end_time = arr[0][1]
cnt = 1
for i in arr:
    if i[0] >= end_time:
        end_time = i[1]
        cnt += 1
print(cnt)