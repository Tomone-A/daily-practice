# ATCoder
# 問題URL: https://atcoder.jp/contests/abc122/tasks/abc122_b

s = str(input())
base = []

def check(i):
    if i == 'A' or i == 'C' or i == 'G' or i == 'T':
        return 1
    else:
        return 0
    
for i in s:
    base.append(check(i)) 

print(base)

# 続きは明日