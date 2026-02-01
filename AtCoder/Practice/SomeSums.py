# Some Sums
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc083_b

n, a, b = map(int, input().split())
# n < 10000
digits = []
d5 = 0
d4 = 0
d3 = 0
d2 = 0
d1 = 0

# 各桁ごとにリストに格納する処理
tmp = n
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

# 今日は一旦終了 これを1から順にn以下まで繰り返す処理にして、
# 各桁の和がA以上B以下のときだけリストに取り出したい。できるかな

print(digits)
