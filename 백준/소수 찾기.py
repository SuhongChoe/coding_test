from itertools import permutations
import sys;input=sys.stdin.readline

def solution(numbers):
    ll=[]
    cnt=0
    for i in range(1,len(numbers)+1): ll+=list(map(int,map(''.join,permutations(numbers,i))))
    ll=list(set(ll))
    for i in ll:
        check=True
        if i<=1:
            check=False
        for j in range(2,int(i**0.5)+1):
            if i%j==0:
                check=False
        if check:
            cnt+=1
    return cnt

solution('011')