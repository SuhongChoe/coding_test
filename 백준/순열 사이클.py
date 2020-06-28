import sys;input=sys.stdin.readline
for _ in range(int(input())):
    input()
    d={ k+1:v for k,v in enumerate(list(map(int, input().split())))}
    for i,c in d.items():
        del d[i]
        d[]