import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
deque=deque([i+1 for i in range(n)])
while len(deque)!=1:
    deque.popleft()
    deque.append(deque.popleft())
print(*deque)