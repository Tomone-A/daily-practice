# Replacing Integer
# 問題URL: https://atcoder.jp/contests/abc161/tasks/abc161_c

n, k = map(int, input().split())
diff = []
tmp = 1
diff.append(n)

while n >= k:
    n = abs(n*tmp - k) 
    diff.append(n)
    tmp += 1
    if n == k:
        n = 0
        break

n = abs(n - k) 
diff.append(n)

print(min(diff))

# 動くけど遅い
# WA1、TLE3