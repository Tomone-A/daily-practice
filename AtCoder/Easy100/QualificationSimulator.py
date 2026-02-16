# Qualification simulator
# 問題URL: https://atcoder.jp/contests/code-festival-2016-qualb/tasks/codefestival_2016_qualB_b

n, a, b = map(int, input().split())
s = list(input())
passlist = [] # 通過者を数えるためのリスト
foreigner = [] # 海外の学生を数えるためのリスト

for i in s:
    if i == 'a': # 国内の学生
        if len(passlist) < a + b:
            passlist.append(i)
            print('Yes')
        else:
            print('No')
    elif i == 'b': # 海外の学生
        foreigner.append(i)
        if len(passlist) < a + b:
            if len(foreigner) <= b:
                passlist.append(i)
                print('Yes')
            else:
                print('No')
        else:
            print('No')
    elif i == 'c': # 学生ではない
        print('No')
    else:
        print('Error')

# AC!