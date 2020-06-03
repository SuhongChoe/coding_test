import sys;input=sys.stdin.readline
ll=[]
for i in range(int(input())):
    a,b=input().split()
    ll.append((int(a),i,b))
for i in sorted(ll,key=lambda x:(x[0],x[1])):
    print(i[0],i[2])