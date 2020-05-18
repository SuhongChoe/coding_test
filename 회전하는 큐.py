from collections import deque
import copy
n,m=map(int,input().split())
ldeque=deque([ i+1 for i in range(n)])
rdeque=copy.deepcopy(ldeque)
ll=map(int,input().split())
cnt=0
for i in ll:
    while True:
        if i == rdeque[0]:
            rdeque.popleft()
            ldeque=copy.deepcopy(rdeque)
            break
        if i == ldeque[0]:
            ldeque.popleft()
            rdeque=copy.deepcopy(ldeque)
            break
        rdeque.append(rdeque.popleft())
        ldeque.appendleft(ldeque.pop())
        cnt+=1
print(cnt)