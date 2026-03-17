# Collatz Problem
# 問題URL: https://atcoder.jp/contests/abc116/tasks/abc116_b

s = int(input())
a = []

def function(n): # 関数の定義
    if n % 2 == 0:
        return n // 2
    else:
        return 3 * n + 1

while(len(a) == len(set(a))): # 値の重複がない間だけ繰り返す
    a.append(s)
    s = function(s)

print(len(a))

# AC!