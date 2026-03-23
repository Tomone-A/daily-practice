# Nice Shopping
# 問題URL: https://atcoder.jp/contests/hitachi2020/tasks/hitachi2020_b

a, b, m = map(int, input().split())
fridge = list(map(int, input().split()))
microwave = list(map(int, input().split()))
coupons = []
for i in range(m):
    coupons.append(list(map(int, input().split())))

price = []

# 割引券を使わない場合の最安値
price.append(min(fridge) + min(microwave))
# すべての組み合わせを試すとMLEになってしまうので、最小値どうしを足し合わせた

# 割引券を使う場合の価格を追加
for coupon in coupons:
    price.append(fridge[coupon[0]-1] + microwave[coupon[1]-1] - coupon[2])

# 最安値を出力
print(min(price))

# AC!