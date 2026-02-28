# Cookie Exchanges
# 問題URL: https://atcoder.jp/contests/agc014/tasks/agc014_a

a, b, c = map(int, input().split())
count = 0

while (a % 2 == 0) and (b % 2 == 0) and (c % 2 == 0):
    if a == b == c :
        print(-1)
        exit()
    ha = a // 2
    hb = b // 2
    hc = c // 2
    a = hb + hc
    b = ha + hc
    c = ha + hb
    count += 1

print(count)

# AC!

# つまずきポイント：無限ループになる条件
# 改善前は、a==b==cのときはもれなく-1が出力されるようにしていた
# これだと奇数枚で同じ枚数の時も無限ループ判定になってしまう
# 同一枚数判定処理をwhile文の中に移動