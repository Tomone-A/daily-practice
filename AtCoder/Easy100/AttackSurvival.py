# Attack Survival
# 問題URL: https://atcoder.jp/contests/abc141/tasks/abc141_c

n, k, q = map(int, input().split())
correct = [ int(input()) for i in range(q) ]

score = k - q # 1回も回答しなかった場合の最低スコアを出しておく

for i in range(1, n+1, 1):
    tmp = 0
    for j in correct:
        if j == i: # 正解数をポイントに加算し、最低スコアと足す
            tmp += 1
    if score + tmp > 0: # 最終的なスコアが0点より高いか判定
        print('Yes')
    else:
        print('No')

# TLE