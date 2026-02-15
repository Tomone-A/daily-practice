# Rally
# 問題URL: https://atcoder.jp/contests/abc156/tasks/abc156_c

n = int(input())
x = list(map(int, input().split()))
p = round(sum(x) / n) 
# pは集会を開く際、消費体力が最小となる座標
# つまり、住人の座標の平均値
# roundは丸め込み（四捨五入）
tai = 0

for i in x:
    tmp = (i - p) ** 2
    tai += tmp

print(tai)

# AC!
