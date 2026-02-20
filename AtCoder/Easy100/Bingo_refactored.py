# Bingo（リファクタリング版）
# 問題URL: https://atcoder.jp/contests/abc157/tasks/abc157_b

# 1. ビンゴカードの取得
card = []
for _ in range(3):
    card.append(list(map(int, input().split())))

# 2. 選ばれた数字の取得
n = int(input())
nums = [int(input()) for _ in range(n)] # リスト内包表記を使って簡潔に

# 3. カードに穴を開ける ('hoge' に書き換え)
for b in nums:
    for row in card:
        for j in range(3):
            if row[j] == b:
                row[j] = 'hoge'

# 4. ビンゴの判定
# ヨコとタテの判定 (ループでまとめて処理)
for i in range(3):
    # ヨコの判定
    if card[i][0] == card[i][1] == card[i][2] == 'hoge':
        print('Yes')
        exit()
    # タテの判定
    if card[0][i] == card[1][i] == card[2][i] == 'hoge':
        print('Yes')
        exit()

# ナナメの判定
if card[0][0] == card[1][1] == card[2][2] == 'hoge':
    print('Yes')
    exit()
if card[0][2] == card[1][1] == card[2][0] == 'hoge':
    print('Yes')
    exit()

# どれにも当てはまらなければ No
print('No')