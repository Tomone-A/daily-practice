# Not Found
# 問題URL: https://atcoder.jp/contests/abc071/tasks/abc071_b

s = list(input()) # 入力を文字ごとに分割して格納
s_ord = list(set(map(ord, s))) # 文字をUnicodeの数値に変換し、重複のないリストにする
s_ord.sort() # 昇順に並び替え

if min(s_ord) != 97: # aが含まれていない場合
    print('a')
    exit()

for i in range(len(s_ord) - 1):
    if s_ord[i+1] - s_ord[i] != 1: # 数値が1ずつ増えていない＝現れていない文字がある
        print(chr(s_ord[i] + 1)) # 辞書順で次に小さい文字を出力
        exit()

if max(s_ord) == 122: # zで終わっている場合
    print('None')
else:
    print(chr(max(s_ord) + 1))