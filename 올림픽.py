import sys;input=sys.stdin.readline
n,k=map(int,input().split())
ll=[]
cnt=1
for _ in range(n):
    country=tuple(map(int,input().split()))
    ll.append(country)
    if country[0] == k:
        a=country
for i in ll:
    if i[1]>a[1]:
        cnt+=1
    elif i[1]==a[1] and i[2]>a[2]:
        cnt+=1
    elif i[1]==a[1] and i[2]==a[2] and i[3]>a[3]:
        cnt+=1
print(cnt)