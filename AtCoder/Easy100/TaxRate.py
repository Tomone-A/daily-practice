# Tax Rate
# 問題URL: https://atcoder.jp/contests/sumitrust2019/tasks/sumitb2019_b

n = int(input())
x = 0

while x <= n: # < ではなく <= にする必要があった！
    if int(1.08 * x) == n: # 税込にした価格がnと一致するとき
        print(x)
        exit()
    x += 1

print(':(')

# AC!