# Chocolate
# 問題URL: https://atcoder.jp/contests/abc092/tasks/abc092_b

n = int(input())
d, x = map(int, input().split())
a = [ int(input()) for i in range(n)]
chocolate = 0

# チョコレートを食べた日にちのリストを参加者ごとに格納する
# リスト内包表記でwhileは使わないらしいけど、range(d)だとちょっと余分かも
a = [ [ i*a[p]+1 for i in range(d) ] for p in range(n)]

for p in range(n): # 参加者p人目について計算を行う
    for i in a[p]:   
        if i > d: # 「i日目」がdを超えたら止める
            break
        else:
            chocolate += 1

print(chocolate + x) 

# AC!