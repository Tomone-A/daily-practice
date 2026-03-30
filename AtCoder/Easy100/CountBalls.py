# Count Balls
# 問題URL: https://atcoder.jp/contests/abc158/tasks/abc158_b

n, a, b = map(int, input().split())

rep = n // (a + b) # 繰り返しの回数
amari = n % (a + b)
ans = 0

if amari <= a:
    ans = rep * a + amari
else:
    ans = rep * a + a

print(ans)

# 一発AC!