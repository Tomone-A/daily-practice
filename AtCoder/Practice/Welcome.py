# A - Welcome to AtCoder
# 問題URL: https://atcoder.jp/contests/abs/tasks/practice_1

# 1行目の整数の入力 (例: 1)
a = int(input())

# 2行目のスペース区切りの整数の入力 (例: 2 3)
b, c = map(int, input().split())

# 3行目の文字列の入力 (例: test)
s = input()

# 計算結果と文字列を出力 (例: 6 test)
print(f"{a + b + c} {s}") # f-string 「フォーマット済み」の新しい書き方
print("{} {}".format(a+b+c, s)) # placeholderを用意し、1つずつ埋め込む方法