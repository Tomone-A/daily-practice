# Bingo
# 問題URL: https://atcoder.jp/contests/abc157/tasks/abc157_b

card = []
for i in range(3):
    tmp = list(map(int, input().split()))
    card.append(tmp)

n = int(input())
nums = []

for i in range(n):
    nums.append(int(input()))

for b in nums: # 番号を1つずつ照らし合わせる
    for i in card: # カードの1行目から順に試す
        for j in range(3):
            if b == i[j]: # 「i行目のj列目」がbと等しいとき
                i[j] = 'hoge'

# card[i][j] 「i行目のj列目」

for i in range(3):
    if card[i][0] == card[i][1] and card[i][1] == card[i][2] and card[i][2] == 'hoge':
        print('Yes')
        exit()

for j in range(3):
    if card[0][j] == card[1][j] and card[1][j] == card[2][j] and card[2][j] == 'hoge':
        print('Yes')
        exit()

if card[1][1] == 'hoge':
    if card[0][0] == card[2][2] and card[0][0] == 'hoge':
        print('Yes')
        exit()
    if card[2][0] == card[0][2] and card[2][0] == 'hoge':
        print('Yes')
        exit()

print('No')

# AC!
# リストの番号指定が1~3ではなく0~2なの忘れがち注意
