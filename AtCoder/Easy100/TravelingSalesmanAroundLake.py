# Traveling Salesman around Lake
# https://atcoder.jp/contests/abc160/tasks/abc160_c

k, n = map(int, input().split())
a = list(map(int, input().split()))
dist = []

# 家どうしの間隔を求める
for i in range(len(a)):
    if i == len(a) - 1: # 0またぎの計算
        dist.append((a[0] + k) - a[i])
    else:
        dist.append(a[i+1] - a[i])

# 間隔の中で最長のものを池の1周から引いた距離が答え
print(k - max(dist))

# AC!(Geminiヒント使用)
# 「歩かなければならない距離の最小化」=「歩かなくていい距離の最大化」と発想を転換させる
