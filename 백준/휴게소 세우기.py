import sys;input=sys.stdin.readline
n,m,k=map(int,input().split())
ll=sorted(list(map(int,input().split())))
def binary():
    global n,m,k
    l=1
    r=k
    while l<=r:
        mid=(l+r)//2
        new=[]
        a=0
        for i in ll:
            cnt = 1
            while i>a+mid*cnt:
                new.append(a+mid * cnt)
                cnt+=1
            a=i
        cnt=1
        while k>a+mid*cnt:
            new.append(a+mid * cnt)
            cnt+=1
        if n+m>=len(set(new+ll)):
            ans=mid
            r=mid-1
        else:
            l=mid+1
    print(ans)
binary()