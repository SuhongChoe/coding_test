import sys;input=sys.stdin.readline
n,m,k=map(int,input().split())
ll=list(map(int,input().split()))
def binary():
    global m
    l=1
    r=max(ll)
    while l<=r:
        temp=''
        mid = (l + r) // 2
        cnt = 0
        for i,c in enumerate(ll):
            if i==0:
                cnt += 1
                temp += '1'
                a = c
                continue
            if c-a>=mid and cnt<m:
                cnt+=1
                temp+='1'
                a=c
            else:
                temp+='0'
        if cnt==m:
            ans=temp
            l=mid+1
        else:
            r=mid-1
    print(ans)

binary()