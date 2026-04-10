# Increment Decrement
# 問題URL: https://atcoder.jp/contests/abc052/tasks/abc052_b

n = int(input())
s = list(input())
x = 0
valuex = [0]

for i in range(n):
    if s[i] == 'I':
        x += 1
        valuex.append(x)
    else:
        x -= 1
        valuex.append(x)

print(max(valuex))

# AC!