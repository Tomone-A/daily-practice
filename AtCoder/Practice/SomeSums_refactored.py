# Some Sums
# 各桁を足し合わせる処理を短く書きたい版

n, a, b = map(int, input().split())

total_sum = 0

for i in range(1, n + 1):
    # 1. 数値を文字列に変換して、各桁の和を計算
    # 解説: str(i)で文字列にし、mapで全文字をint化し、sumで合計
    digit_sum = sum(map(int, str(i)))
    
    # 2. 条件チェック
    if a <= digit_sum <= b:
        total_sum += i

print(total_sum)

# intをstrにして、またintに戻すだけで桁ごとに分解できるのはなぜ？？
# str(文字列型)はリストと同じように扱えるから、map関数で1文字ずつ処理できる！