# Otoshidama
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc085_c

n, sum = map(int, input().split())
x = 0
y = 0
z = 0

for p in range(n + 1):
    for q in range(n + 1 - p):
        z = n - (p + q)
        if p * 10000 + q * 5000 + z * 1000 == sum:
            x = p
            y = q
            print(x, y, z)
            exit()
        else:
            x = -1
            y = -1
            z = -1

print(x, y, z)

# AC （Geminiヒント使用）