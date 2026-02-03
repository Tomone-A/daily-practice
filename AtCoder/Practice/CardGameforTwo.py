# Card Game for Two
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc088_b

n = int(input())
cards = list(map(int, input().split()))
cards_d = sorted(cards, reverse=True) # 降順（点数順）に並び替える

point_alice = 0
point_bob = 0

# 点数が高いカードから互いに取っていく処理
for i in range(0, len(cards_d), 2):
    point_alice += cards_d[i]
    if i+1 >= len(cards_d):
        break # カードが奇数枚のとき、Aliceの番で終わるようにする
    else:
        point_bob += cards_d[i+1]

print(point_alice - point_bob)

# AC!