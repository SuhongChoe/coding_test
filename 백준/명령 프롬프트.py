import sys;input=sys.stdin.readline
s=''
for _ in range(int(input())):
    a = input().strip()
    for i in range(len(s)):
        if s[i]!=a[i]:
            a=a[:i]+'?'+a[i+1:]
    s=a
print(s)