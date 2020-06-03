import sys;input = sys.stdin.readline
country = sorted([tuple(map(int, input().split())) for _ in range(int(input()))], key=lambda x: -x[2])
d={}
cnt=0
for i in country:
    try:
        if d[i[0]]>=2:
            continue
        d[i[0]]+=1
    except:
        d[i[0]]=1
    if cnt>=3:
        break
    print(i[0],i[1])
    cnt+=1