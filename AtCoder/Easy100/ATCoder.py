# ATCoder
# 問題URL: https://atcoder.jp/contests/abc122/tasks/abc122_b

s = str(input())
base = []

# 文字列の中でACGTが連続する長さの最長を求める
# 該当すればリストの末尾の値に1を足し、該当しなければリストの末尾に0を追加する
# リストの値のうち最大のものが答え
for i in range(len(s)):
    if s[i] == 'A' or s[i] == 'C' or s[i] == 'G' or s[i] == 'T':
        if base == []:
            base.append(1)
        elif base[-1] == 0 :
            base.append(1)
        else:
            base[-1] += 1
    else:
        base.append(0)

print(max(base))

# AC!