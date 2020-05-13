import sys;input=sys.stdin.readline
s1,s2=list(input().strip()),[]
for _ in range(int(input())):
    cmd=input().split()
    if cmd[0]=='L' and s1:
        s2.append(s1.pop())
    elif cmd[0]=='D' and s2:
        s1.append(s2.pop())
    elif cmd[0]=='B' and s1:
        s1.pop()
    elif cmd[0]=='P':
        s1.append(cmd[1])
print(''.join(s1+s2[::-1]))