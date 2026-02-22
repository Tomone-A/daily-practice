# 1 21
# 問題URL: http://atcoder.jp/contests/abc086/tasks/abc086_b
import math

a, b = map(str, input().split())
s = int(a + b) # 文字列として入力し、結合する

# 平方根は0.5乗で求められる
if int(s ** 0.5) == (s ** 0.5): # 小数部分が0のとき
    print('Yes')
else:
    print('No')

# AC!