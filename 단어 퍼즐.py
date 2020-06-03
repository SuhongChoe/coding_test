import sys;input=sys.stdin.readline
from collections import Counter
cnt=1
while True:
    same=False
    a=input().strip()
    b=input().strip()
    if a=='END' and b=='END':
        break
    if Counter(a)==Counter(b):
        same=True
    if same: print('Case {}: same'.format(cnt))
    else: print('Case {}: different'.format(cnt))
    cnt+=1