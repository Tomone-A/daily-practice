# Count Order
# 問題URL: https://atcoder.jp/contests/abc150/tasks/abc150_c
import itertools

n = [ i+1 for i in range(int(input()))]
p = list(map(int, input().split()))
q = list(map(int, input().split()))

dict = list(itertools.permutations(n))
dict = [ list(i) for i in dict ] # 辞書探索用に、タプルからリストに変換

pnum = 0
qnum = 0

for i in range(len(dict)):
    if dict[i] == p:
        pnum = i+1
        if dict[i] == q: # たぶん冗長だけど、pとqが同じだった場合の処理
            qnum = i+1 
    elif dict[i] == q:
        qnum = i+1
    else:
        pass

print(abs(pnum - qnum))

# AC!