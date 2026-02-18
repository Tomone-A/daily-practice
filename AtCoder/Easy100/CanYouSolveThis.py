# Can you solve this?
# 問題URL: https://atcoder.jp/contests/abc121/tasks/abc121_b

n, m, c = map(int, input().split())
codes = [] 

b = list(map(int, input().split()))

for i in range(n):
    tmp = list(map(int, input().split()))
    codes.append(tmp) # n個のソースコードは、配列の配列として格納する

count = 0 # 正答するコードを数える変数

for code in codes: # コードを1つずつ確かめる
    sum = 0
    for i in range(m):
        sum += code[i] * b[i] # codeのi番目とbのi番目を掛け合わせて合計に足す
    sum += c # 最後にcを足す
    if sum > 0:
        count += 1
    else:
        pass

print(count)

# 一発AC!!