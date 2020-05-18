import sys;input=sys.stdin.readline
from bisect import *
while input()!="":
    arr=[float('inf')]
    ll=list(map(int,input().split()))
    for i in ll:
        a=bisect_left(arr,i)
        if a>=len(arr):
            arr.append(i)
        else:
            arr[bisect_left(arr,i)]=i
    print(len(arr))