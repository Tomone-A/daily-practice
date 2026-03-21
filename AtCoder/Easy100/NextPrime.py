# Next Prime
# 問題URL: https://atcoder.jp/contests/abc149/tasks/abc149_c

x = int(input())
count = 0

def primecheck(num):
    for i in range(2, num - 1, 1):
        if x % i == 0:
            return False
    return True

while(primecheck(x) == False):
    x += 1

print(x)

# AC!