# Attack Survival
# 問題URL: https://atcoder.jp/contests/abc141/tasks/abc141_c

n, k, q = map(int, input().split())
correct = [ int(input()) for i in range(q) ]

score = k - q # 1回も回答しなかった場合の最低スコアを出しておく

correct_counts = [0] * n # 各人の正解数を格納するリスト

for i in correct:
    correct_counts[i-1] += 1

for i in correct_counts:
    if score + i > 0:
        print('Yes')
    else:
        print('No')

# AC!