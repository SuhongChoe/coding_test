import sys
input=sys.stdin.readline
n=int(input())
list=[i+1 for i in range(n)]
ans=[]
while len(list)!=0:
    ans.append(list.pop(0))
    if len(list)!=0:
        list.append(list.pop(0))
print(*ans)