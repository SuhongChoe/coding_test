import sys;input=sys.stdin.readline
from bisect import bisect_left
input()
n=int(input())
ll=sorted([tuple(map(int,input().split())) for i in range(int(input()))],key=lambda x : x[1])
def binary():
    global n
    l=max(ll,key=lambda x: x[0])[0]
    r=max(ll,key=lambda x : x[1])[1]
    while l<=r:
        cnt=1
        mid=(l+r)//2
        a=ll[0][1]
        for i in ll:
            if i[1]>=a+mid:
                a=i[1]
                cnt+=1
        if n>=cnt:
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)
binary()