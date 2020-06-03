cmd=input()
d={1:1,2:0,3:0}
for i in cmd:
    if i=='A':
        d[1],d[2]=d[2],d[1]
    elif i=='B':
        d[2],d[3]=d[3],d[2]
    else:
        d[1],d[3]=d[3],d[1]
for i in d.keys():
    if d[i]:
        print(i)