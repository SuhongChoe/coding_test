import sys
input=sys.stdin.readline
input()
s=set(map(int,input().split()))
input()
list=map(int,input().split())
for i in list:
    if i in s:
        print(1,end = ' ')
    else:
        print(0,end = ' ')