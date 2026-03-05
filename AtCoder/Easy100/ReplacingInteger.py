# Replacing Integer
# 問題URL: https://atcoder.jp/contests/abc161/tasks/abc161_c

n, k = map(int, input().split())
tia = []

n = n % k
m1 = abs(n - k)
m2 = abs(m1 - k)

tia.append(m1)
tia.append(m2)

print(min(tia))

# AC!(Geminiヒント使用)
# 割り算の"あまり"、算数においては使わないがちだけどプログラミングにおいてはありえん価値が高い