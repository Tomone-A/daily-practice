# Some Sums
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc083_b

n, a, b = map(int, input().split())

nums = []

# 各桁ごとにリストに格納する処理
# n < 10000 という制約を利用
def digsplit(x, y, z):
    tmp = x
    digits = []
    d5 = 0
    d4 = 0
    d3 = 0
    d2 = 0
    d1 = 0
    s = 0
    d5 = tmp // 10000
    digits.append(d5)
    tmp = tmp - (d5 * 10000)
    d4 = tmp // 1000
    digits.append(d4)
    tmp = tmp - (d4 * 1000)
    d3 = tmp // 100
    digits.append(d3)
    tmp = tmp - (d3 * 100)
    d2 = tmp // 10
    digits.append(d2)
    tmp = tmp - (d2 * 10)
    d1 = tmp // 1
    digits.append(d1)
    tmp = tmp - (d1 * 10)
    # 「A以上B以下」の処理
    if y <= sum(digits) <= z :
        nums.append(x)

# nまで全部試す
for i in range(n + 1) :
    digsplit(i, a, b)

print(sum(nums))

# AC！