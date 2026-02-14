# Candy Distribution Again
# 問題URL: https://atcoder.jp/contests/agc027/tasks/agc027_a

n, x = map(int, input().split())
a = list(map(int, input().split())) # list関数を使えば入力個数を決めなくてよい！
count = 0

children = sorted(a) # 昇順に並び替え

if children[0] > x:
    print(count)
    exit()

for i in range(n):
    if i == n-1: # 最後に多めにもらった子が喜んでしまう問題を解決したい
        if children[i] == x: 
            count += 1 # 最後がぴったりなら満足
            break
        else:
            break
    x = x - children[i]
    if x == 0:
        count += 1
        break
    if x < 0:
        break
    count += 1

print(count)

# AC!