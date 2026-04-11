# Postal Code
# 問題URL: https://atcoder.jp/contests/abc084/tasks/abc084_b

a, b = map(int, input().split())
s = list(input())

if len(s) != a + b + 1:
    print('No')
    exit()

for i in range(len(s)):
    if i == a:
        if s[i] != '-':
            print('No')
            exit()
    elif s[i] == '-':
        print('No')
        exit()
        
print('Yes')

# AC!