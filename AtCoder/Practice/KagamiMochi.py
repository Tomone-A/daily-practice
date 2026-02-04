# Kagami Mochi
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc085_b

# 半径をリストに格納して、重複を削除する機能があればできそう

n = int(input())
mochi = []

for i in range(n): # n回だけ入力を受け付ける処理
    mochi.append(int(input()))

mochimochi = list(set(mochi)) # setは重複を許さないデータ構造

print(len(mochimochi))

# AC!