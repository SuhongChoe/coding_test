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
        cnt=1
        temp=0
        for i in ll:
            if bluelay+i>mid:
                temp=max(bluelay,temp)
                cnt+=1
                bluelay=i
            else:
                bluelay+=i
        temp = max(bluelay, temp)
        if cnt<=m:
            r=mid-1
            ans=mid
        else:
            l=mid+1
    return ans

print(binary())