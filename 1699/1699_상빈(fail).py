N = int(input())

n = 1

num_list = []

while n**2 <= N:                                # N보다 작은 제곱수들을 구하는 while문
    num_list.append(n**2)
    n += 1

cnt = 0

while N > 0:                                    # N이 아직 남아있을 경우 반복
    for i in range(len(num_list)-1, -1, -1):
        if num_list[i] <= N:                    # N과 같거나 / N보다 작은 제곱수 중 가장 큰 수를 찾아서    
            cnt += 1                            # cnt를 1 추가시키고
            N -= num_list[i]                    # N을 그만큼 감소시킨다.
            break                               # for문 이탈

print(cnt)