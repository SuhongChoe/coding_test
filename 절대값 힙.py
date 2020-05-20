import sys
import heapq
input=sys.stdin.readline
heap=[]
for _ in range(int(input())):
    n=int(input())
    if n==0:
        if len(heap)==0:
            print(0)
        else:
            print(heapq.heappop(heap)[1])
    else:
        heapq.heappush(heap,(abs(n),n))