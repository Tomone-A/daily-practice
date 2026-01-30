# Shift Only
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc081_b

res = True # 全て偶数かどうか
n = int(input())
a = input().split()
a_int = [int(i) for i in a] # int型に変換
count = 0 # 操作の回数

# 2で割る機能
def half(x):
    return int(x / 2)

# リストの中身が全部偶数かどうか調べる
def checkeven(li):
    for i in li :
        if i % 2 == 0:
            pass
        else :
            return False
            break
    return True

while res == True: # リストの要素がすべて偶数の間だけ繰り返す
    res = checkeven(a_int) # 偶数かどうか判定
    if res == True: 
        for i in range(len(a_int)) :
            a_int[i] = half(a_int[i])
        count += 1

print(count)

# AC!（たぶん想定解ではない...）