import sys;input=sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())

A = list(map(lambda x : x-B, A))

people = len(A)

for i in A:
    if i>0:
        people+=i//C+1 if i%C!=0 else i//C

print(people)