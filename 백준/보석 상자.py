import sys;input=sys.stdin.readline
n,m=map(int,input().split())
ll=sorted([int(input()) for i in range(m)])
def binary():
    global n,m
    l=1
    r=max(ll)
    ans=r
    while l<=r:
        mid=(l+r)//2
        cnt=0
        for i in range(m):
            cnt += -((-ll[i]) // mid)
        if cnt<=n:
            ans = min(ans,mid)
            r=mid-1
        else:
            l=mid+1
    return ans
print(binary())