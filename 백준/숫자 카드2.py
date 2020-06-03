import sys
from collections import Counter
input=sys.stdin.readline
input()
cnt=Counter(map(int,input().split()))
input()
list=map(int,input().split())
for i in list:
    print(cnt[i],end=' ')