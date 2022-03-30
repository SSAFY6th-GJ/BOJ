# 처음부터 9876 이런 숫자 넣으려 하지말고 각 알파벳의 자릿수를 파악하자
# GCF
# ACDEB
# 이 있을때 A는 10000의 자리, C는 1000+10 의 자리, G는 100의 자리..이렇게 자릿수를 파악한 다음에
# 그 자릿수를 list로 받고 내림차순으로 정리한 후에 9부터 1씩 빼주면서 더해주자.
N = int(input())
res = 0
dic = {}
num_lst = []
for _ in range(N):
    num = input()
    for i in range(len(num)):
        if num[i] not in dic.keys():
            dic[num[i]] = 10 ** (len(num)-i-1)
        else:
            dic[num[i]] += 10 ** (len(num)-i-1)
for x in dic.values():
    num_lst.append(x)
num_lst.sort(reverse=True)
res = 0
start = 9
for i in num_lst:
    res += start * i
    start -= 1
print(res)