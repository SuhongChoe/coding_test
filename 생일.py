import sys;input=sys.stdin.readline
ll=[tuple(input().split()) for _ in range(int(input()))]
print(sorted(ll,key=lambda x:(-int(x[3]),-int(x[2]),-int(x[1])))[0][0])
print(sorted(ll,key=lambda x:(int(x[3]),int(x[2]),int(x[1])))[0][0])