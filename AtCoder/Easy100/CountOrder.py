# Count Order
# 問題URL: https://atcoder.jp/contests/abc150/tasks/abc150_c

n = int(input())
p = list(map(int, input().split()))
q = list(map(int, input().split()))

dict = []

for i in range(n):
    tmp = []
    for j in range(n):
        tmp.append(j+1)
    dict.append(tmp)

print(dict)