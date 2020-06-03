import sys;input=sys.stdin.readline
n=int(input())
ll=[int(input()) for _ in range(n)]
temp=[]
temp1=[]
ans=[]
cnt=0
i=1
while temp1 != ll:
    if ll[cnt] in temp:
        if temp[-1]==ll[cnt]:
            cnt+=1
            temp1.append(temp.pop())
            ans.append('-')
        else:
            ans=["NO"]
            break
    else:
        temp.append(i)
        i+=1
        ans.append('+')
if len(ans)==1:
    print(*ans)
else:
    for i in ans:
        print(i)