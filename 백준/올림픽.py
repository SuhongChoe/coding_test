import sys;input=sys.stdin.readline
n,k=map(int,input().split())
ll=[tuple(map(int,input().split())) for _ in range(n)]
ans=sorted(ll,key=lambda x:(-x[1],-x[2],-x[3]))
cnt=1
v=[ans[0][1],ans[0][2],ans[0][3]]
for i in ans:
    if v!=[i[1],i[2],i[3]]:
        v=[i[1],i[2],i[3]]
        cnt+=1
    if i[0]==k:
        print(cnt)