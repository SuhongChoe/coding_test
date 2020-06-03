import sys
import heapq
input=sys.stdin.readline
heap=[]
n=int(input())
list=[ int(input()) for i in range(n)]
for i in list:
    if i == 0:
        if len(heap) == 0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(-i,i))