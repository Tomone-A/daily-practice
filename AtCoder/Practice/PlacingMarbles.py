# Placing Marbles
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc081_a

si = []
si = list(input()) # スペースなしで入力値を分割、リストに格納する
count = 0

for i in si :
    if i == '1' :
        count += 1
    
print(count)

# AC!
