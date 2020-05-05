import sys
input=sys.stdin.readline
input()
print(*sorted(set(map(int,input().split()))))