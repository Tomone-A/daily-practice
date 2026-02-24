# Collecting Balls (Easy Version)
# 問題URL: https://atcoder.jp/contests/abc074/tasks/abc074_b

n = int(input())
k = int(input()) # 数直線の端
x = list(map(int, input().split()))
dist = 0

for i in range(n):
    if x[i] > k // 2 : 
        # bのロボットが回収する
        dist += (k - x[i]) * 2
    else: 
        # aのロボットが回収する
        dist += x[i] * 2

print(dist)

# AC!