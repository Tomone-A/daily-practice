# Go to School
# 問題URL: https://atcoder.jp/contests/abc142/tasks/abc142_c

n = int(input())
students = list(map(int, input().split()))
numbers = []

# 来た順番を格納するリストを作る
for i in range(len(students)):
    numbers.append('hoge')

# 生徒の出席番号順に、来た順番を所定の位置に当てはめていく
for i in range(len(students)):
    # 0オリジンのため調整が必要
    numbers[students[i]- 1] = i + 1

# リスト形式の出力ではなく、スペースで区切るだけにする
order = [str(i) for i in numbers] # joinを使うには文字列への変換が必要
order = ' '.join(order)
print(order)

# AC!