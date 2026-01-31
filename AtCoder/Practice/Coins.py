# Coins
# 問題URL: https://atcoder.jp/contests/abs/tasks/abc087_b

count = 0

gohyaku = int(input())
hyaku = int(input())
goju = int(input())

sum = int(input())

# 効率的に計算しようとするとわけわかんなくなったので、しらみつぶし作戦
# 持っている硬貨を全パターン足し合わせて、ちょうど合計金額になるパターンを数える

for a in range(gohyaku + 1):
    for b in range(hyaku + 1):
        for c in range(goju + 1):
            if 500 * a + 100 * b + 50 * c == sum:
                count += 1

print(count)

# AC!（Geminiにヒント聞いた）