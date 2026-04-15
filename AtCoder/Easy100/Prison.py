# Prison
# 問題URL: https://atcoder.jp/contests/abc127/tasks/abc127_c

n, m = map(int, input().split())
l = []
r = []

for i in range(m):
    a, b = map(int, input().split())
    l.append(a)
    r.append(b)

left = max(l)
right = min(r)

# 最も厳しい下限（lの最大）と最も厳しい上限（rの最小）の間を数える

if right - left + 1 >= 0:
    print(right - left + 1)
else:
    print(0)

# AC!(Geminiヒント使用)
