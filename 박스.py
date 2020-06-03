import sys;input=sys.stdin.readline
for _ in range(int(input())):
    sum=0
    m,n=map(int,input().split())
    ll=[ list(map(int,input().split())) for i in range(m)]
    box_end=[ 0 for i in range(n)]
    for i in range(m-1,-1,-1):
        for j in range(n):
            if ll[i][j]==1:
                sum+=m-1-i-box_end[j]
                box_end[j] += 1
    print(sum)