# Five Dishes
# 問題URL: https://atcoder.jp/contests/abc123/tasks/abc123_b
import math

time = 0
dishes = [int(input()) for i in range(5)]
last_digit = [(i % 10) for i in dishes]
last_digit = [i for i in last_digit if i != 0] # 割り切れるものを削除
last_order = 0
if last_digit != []: # 割り切れないものが1つでもあれば
    last_order = 10 - min(last_digit)

for d in dishes:
    tmp = (math.ceil(d / 10)) * 10 # 下1桁を切り上げ
    time += tmp

print(time - last_order)

# AC!