import sys
input=sys.stdin.readline
T=int(input())
for i in range(T):
    N=int(input())
    N_list=input().split()
    M = int(input())
    M_list = input().split()
    s=set(N_list)
    for j in M_list:
        if j in s:
            print(1)
        else:
            print(0)