from collections import Counter
a=int(input())
b=int(input())
c=int(input())
d=Counter(list(str(a*b*c)))
l=[str(i) for i in range(0,10)]
for i in l:
    print(d[i])