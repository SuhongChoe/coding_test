import sys;

input = sys.stdin.readline
ll = [int(input()) for _ in range(int(input()))]
temp = []
ans = ""
cnt = 0
p = True
i = 1
while cnt < len(ll):
    if i > ll[cnt]:
        if temp[-1] == ll[cnt]:
            cnt += 1
            temp.pop()
            ans += '-\n'
        else:
            p = False
            break
    else:
        temp.append(i)
        i += 1
        ans += '+\n'
if p:
    print(ans, end='')
else:
    print("NO")
