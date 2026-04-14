# Prison
# 問題URL: https://atcoder.jp/contests/abc127/tasks/abc127_c

n, m = map(int, input().split())
cards = []

for i in range(m):
    l, r = map(int, input().split())
    cards.append([l, r])

numbers = []

for card in cards:
    for i in range(card[0], card[1] + 1, 1):
        numbers.append(i)

count = 0

for i in range(n):
    tmp = numbers.count(i)
    if tmp == m:
        count += 1

print(count)

# 桁数が増えると計算に時間がかかりTLEに