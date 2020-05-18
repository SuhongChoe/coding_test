import sys;input=sys.stdin.readline
for _ in range(int(input())):
    input()
    A=sorted(map(int,input().split()))
    B=sorted(map(int,input().split()))
    sum=0
    while A:
        while B and A[-1]<=B[-1]:
            B.pop()
        sum+=len(B)
        A.pop()
    print(sum)