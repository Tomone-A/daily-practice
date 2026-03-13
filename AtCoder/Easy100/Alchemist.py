# Alchemist
# 問題URL: https://atcoder.jp/contests/abc138/tasks/abc138_c

n = int(input())
value = list(map(int, input().split()))

# 具材の価値が最大化するとき→最も大きな価値を持つ具材を最後に合成した時
# 昇順に並び替えてから合成を繰り返す
value = sorted(value)

# 具材の合成を繰り返す処理を書く
while(n > 1):
    value.append((value[0] + value[1]) / 2)
    del value[0]
    del value[0]
    value = sorted(value)
    n = len(value)

print(value[0])

# AC!