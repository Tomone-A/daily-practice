# Bishop
# 問題URL: https://atcoder.jp/contests/panasonic2020/tasks/panasonic2020_b
import math

h, w = map(int, input().split())

# 片方の辺が1の場合、どこにも動けないので除外する
if h == 1 or w == 1:
    print(1)
    exit()
else:
    print(math.ceil((h * w) / 2)) # ceil=天井。切り上げのこと

# AC!