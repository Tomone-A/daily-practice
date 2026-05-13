# Exception Handling
# 問題URL: https://atcoder.jp/contests/abc134/tasks/abc134_c

n = int(input())
nums = [ int(input()) for i in range(n)]
nums_order = sorted(nums, reverse=True)
# 最大値以外は最大値を出力し、最大値のときは2番目に大きな値を出力する

for num in nums:
    if num == max(nums):
        print(nums_order[1])
    else:
        print(nums_order[0])

# TLEになってしまう