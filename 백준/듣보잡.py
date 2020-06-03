import sys
input=sys.stdin.readline
n,m=map(int,input().split())
list1=[input().strip() for i in range(n)]
list2=[input().strip() for i in range(m)]
ans=list(set(list1)&set(list2))
print(len(ans))
for i in sorted(ans):
    print(i)