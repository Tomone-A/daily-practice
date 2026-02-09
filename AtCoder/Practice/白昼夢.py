# 白昼夢
# 問題URL: https://atcoder.jp/contests/abs/tasks/arc065_a

s = str(input())

# replace()メソッドで、指定した文字列に完全一致する文字列を削除できる
# s.replace('aaa', '')のように、空の文字列''に置換する
# ただし、消す順番は気をつけないといけない
# dreamerはdreamを、eraserはeraseを包含するため、前者の長い単語から消さないとerが残ってしまう。
# dreameraserのような文字列の場合、dreamerをeraseやeraserより先に消すとrase, raserが残ってしまう。
# よって最適な消し順はeraser > erase > dreamer > dream

s = s.replace('eraser', '')
s = s.replace('erase', '')
s = s.replace('dreamer', '')
s = s.replace('dream', '')

if s == '':
    print('YES')
else:
    print('NO')

# AC!