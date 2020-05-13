stack = []
ans = []
input()
top = list(map(int, input().split()))
for i in range(len(top)):
    while stack:
        if stack[-1][1] > top[i]:
            ans.append(stack[-1][0] + 1)
            break
        stack.pop()
    if not stack:
        ans.append(0)
    stack.append([i,top[i]])
print(*ans)