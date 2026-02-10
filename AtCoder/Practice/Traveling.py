# Traveling
# 問題URL: https://atcoder.jp/contests/abs/tasks/arc089_a

n = int(input())
t = []
x = []
y = []

for i in range(n):
    t_tmp, x_tmp, y_tmp = map(int, input().split())
    t.append(t_tmp)
    x.append(x_tmp)
    y.append(y_tmp)

# 1回目の移動で弾く処理
if x[0] + y[0] > t[0]:
    print('No')
    exit()
elif x[0] + y[0] % 2 == 0: #偶奇の一致判定:移動距離が偶数のとき
    if t[0] % 2 != 0: #奇数回では到達不可
        print('No')
        exit()
else: #移動距離が奇数のとき
    if t[0] % 2 == 0:  #偶数回では到達不可
        print('No')
        exit()

# 2回目以降は繰り返し処理
for i in range(n):
    if i == n-1:
        break
    time = t[i+1] - t[i]
    dx = abs(x[i+1] - x[i]) # absは絶対値関数
    dy = abs(y[i+1] - y[i])
    dist = dx + dy # 移動距離の総和を出す
    if dist > time:
        print('No')
        exit()
    elif dist % 2 == 0: #偶奇の一致判定:移動距離が偶数のとき
        if time % 2 != 0: #奇数回では到達不可
            print('No')
            exit()
    else: #移動距離が奇数のとき
        if time % 2 == 0:  #偶数回では到達不可
            print('No')
            exit()

print('Yes')

# AC!
# AtCoder Beginners Selection 全クリア