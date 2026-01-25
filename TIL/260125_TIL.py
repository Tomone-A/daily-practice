# 260125_TIL
# map関数の勉強

# チュートリアル　
# 参考:https://www.adecco.com/ja-jp/useful/engineer/explain-pythons-map-function

sample1_list = list(range(5))

def multi(x):
    y = x * 2
    return y

sample2_list = map(multi, sample1_list)

print(list(sample2_list))

sample1_list = [1, 2, 3]
sample2_list = [4, 5, 6]

def myfunc(i, j):
    return (i, j)

print(list(map(myfunc, sample1_list, sample2_list)))

# 疑問：配列のリストから要素数を返すプログラムは書ける？

sample1_list = [[1, 2, 3], [4, 5, 6, 7], [8, 9]]
sample2_list = [["しずけさや"], ["いわにしみいる"], ["せみのこええええ"]]

def count(x):
    return len(x)

sample3_list = map(count, sample1_list)
sample4_list = map(count, sample2_list)

print(list(sample3_list))
print(list(sample4_list))

# 数字は数えられるけど、文字列だと[1, 1, 1]になってしまう。
# 1文字ずつ分割して数える必要あり

def count_char(x):
    print(x[0]) # 0文字目を表示しているのではなく、配列の最初の文字列を取り出している
    return len(x[0])

sample4_list = map(count_char, sample2_list)

print(list(sample4_list))

# 用語の勉強

# 参考: https://qiita.com/bkh4149/items/fa7c80e4d7077aa609c1
# イテレーション：繰り返し処理のこと
# イテラブル：繰り返し処理での参照元。for i in sample_list なら sample_list。
# イテレータ：繰り返し処理の結果を格納しているオブジェクト。

a = [1, 2, 3, 4, 5] # aはイテラブル
it = iter(a) # itはイテレータ
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it)) # 弾切れになると、StopIterationエラーになる