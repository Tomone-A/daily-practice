# Otoshidama
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc085_c

maisu = int(input())
sum = int(input())
x = 0
y = 0
z = 0

for p in range(maisu + 1):
    for q in range(maisu + 1):
        for r in range(maisu + 1):
            if p*10000 + q*5000 + r*1000 == sum and p+q+r == maisu:
                x = p
                y = q
                z = r
                break
            else:
                x = -1
                y = -1
                z = -1

print(x, y, z)

# わからんので明日に持ち越します
# ヒントほしい
