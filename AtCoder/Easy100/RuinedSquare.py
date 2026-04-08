# Ruined Square
# 問題URL: https://atcoder.jp/contests/abc108/tasks/abc108_b

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = 0, 0, 0, 0
gradx = x2 - x1
grady = y2 - y1

x3 = x2 + (grady * -1)
y3 = y2 + (gradx)
x4 = x3 + (gradx * -1)
y4 = y3 + (grady * -1)

print(x3, y3, x4, y4)

# AC!