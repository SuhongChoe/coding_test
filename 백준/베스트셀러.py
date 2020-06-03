import sys,collections;input=sys.stdin.readline
d=collections.Counter([input().strip() for _ in range(int(input()))])
print(sorted(d.keys(),key=lambda x:(-d[x],x))[0])
