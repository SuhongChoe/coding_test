import sys;input=sys.stdin.readline
n,m=map(int,input().split())
ll=list(map(int,input().split()))

def binary():
    global m
    l=1
    r=sum(ll)
    ans=0
    while l<=r:
        mid=(l+r)//2
        bluelay=0
        temp=0
        cnt = 1
        for i in ll:
            if temp+i>mid:
                cnt+=1
                bluelay=max(bluelay,temp)
                temp=i
            else:
                temp+=i
        if cnt<=m:
            ans=max(mid,bluelay,temp)
            r=mid-1
        else:
            l=mid+1
    print(ans)

binary()