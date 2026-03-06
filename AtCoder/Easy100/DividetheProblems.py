# Divide the Problems
# 問題URL: https://atcoder.jp/contests/abc132/tasks/abc132_c

n = int(input()) # dの長さ
d = list(map(int, input().split()))
d.sort() # 昇順に並び替える → リストの真ん中で2つに割れる
print(d[n // 2] - d[n // 2 - 1]) 

# AC!
# 整数Kは、真ん中2つの値の間で定まる。0なら存在しない。
# よって答えは『dの[半分(大きい方)]番目 - dの[半分(小さい方)]番目』