import sys;input=sys.stdin.readline
n,m=map(int,input().split())
d={}
ans=0
for i in range(n):
    s=input().strip()
    try:
        d[s]+=1
    except:
        d[s]=1
k=int(input())
for i in d:
    cnt = i.count('0')
    if cnt<=k and cnt%2==k%2:
        ans=max(ans,d[i])
print(ans)