# Break Number
# 問題URL: https://atcoder.jp/contests/abc068/tasks/abc068_b

n = int(input())
a = 1
li = []

# 求められているのは「n以下で最大の2の乗数」
while a <= n :
    li.append(a)
    a = a * 2

print(max(li))

# AC!