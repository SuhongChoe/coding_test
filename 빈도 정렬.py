import sys;input=sys.stdin.readline
input()
d={}
cnt=0
ll=list(map(int,input().split()))
for i in ll:
    try:
        d[i][0]+=1
    except:
        d[i]=[1,cnt]
        cnt+=1
for i in sorted(d.items(),key=lambda x:(-x[1][0],x[1][1])):
    for _ in range(i[1][0]):
        print(i[0],end=" ")