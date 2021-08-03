import sys;input=sys.stdin.readline
from collections import deque

N = int(input())

K = int(input())
apple = [ tuple(map(int,input().split())) for _ in range(K)]

L = int(input())
change_direction = list(reversed([input().split() for _ in range(L)]))

y = deque([0,-1,0,1])
x = deque([1,0,-1,0])

cur_x,cur_y = 1,1
cur_snake = deque([(1,1)])
time = 0

while (cur_x >= 1 and cur_x <= N) and (cur_y >=1 and cur_y <=N):
    if change_direction and int(change_direction[-1][0])==time:
        # 방향 회전
        if change_direction[-1][1] == 'D':
            x.rotate(1)
            y.rotate(1)
        if change_direction[-1][1] == 'L':
            x.rotate(-1)
            y.rotate(-1)
        change_direction.pop()

    time += 1
    cur_x += x[0]
    cur_y += y[0]

    if (cur_y,cur_x) in set(cur_snake):break

    cur_snake.append((cur_y,cur_x))

    flag = True
    # 사과 있을 때
    if (cur_y,cur_x) in apple:
        flag = False
        #print(apple)
        apple.remove((cur_y,cur_x))
    # 사과 없을 때
    if flag:
        cur_snake.popleft()

print(time)
