# Power Socket
# 問題URL: https://atcoder.jp/contests/abc139/tasks/abc139_b

a, b = map(int, input().split())
sockets = a
taps = 1 # 最初のタップを使う

if b == 1: # タップが必要ない場合
    print(0)
    exit()

while sockets < b :
    taps += 1
    sockets = sockets + a - 1 # 1口犠牲にしてa口増やす

print(taps)

# AC!