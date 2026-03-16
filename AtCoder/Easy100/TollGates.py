# Toll Gates
# 問題URL: https://atcoder.jp/contests/abc094/tasks/abc094_b

n, m, x = map(int, input().split())
a = list(map(int, input().split()))

tg = []
[ tg.append(0) for i in range(n + 1) ]
# 料金所の位置にだけ1を代入し、コストを設定する
for i in range(m):
    tg[a[i]] = 1

# 0に向かうルートとNに向かうルートのそれぞれでコストを計算する
path_zero = 0
path_n = 0
for i in range(n + 1):
    if i <= x:
        path_zero += tg[i]
    else:
        path_n += tg[i]

# 両者を比較して小さい方が答え
print(min(path_zero, path_n))

# 一発AC!