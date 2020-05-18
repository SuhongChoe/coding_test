import sys;input = sys.stdin.readline

def dfs(idx, sum):
    global cnt
    if idx>=n:
        return
    sum+=ll[idx]
    if sum==s:
        cnt+=1
    dfs(idx + 1, sum - ll[idx])
    dfs(idx+1,sum)

cnt = 0
n, s = map(int, input().split())
ll = list(map(int, input().split()))
dfs(0, 0)
print(cnt)