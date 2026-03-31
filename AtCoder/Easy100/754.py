# 754
# 問題URL: https://atcoder.jp/contests/abc114/tasks/abc114_b

s = list(str(input()))
x = []

for i in range(len(s) - 2):
    x.append(int(s[i] + s[i+1] + s[i+2]))

x_dif = []

for num in x:    
    x_dif.append(abs(753 - num))

print(min(x_dif))

# AC!