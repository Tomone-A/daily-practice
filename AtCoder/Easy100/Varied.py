# Varied
# 問題URL: https://atcoder.jp/contests/abc063/tasks/abc063_b

s = list(input()) # 文字ごとに分割してリストに格納
s_set = set(s)

if len(s) == len(s_set):
    print('yes')
else:
    print('no')

# AC!