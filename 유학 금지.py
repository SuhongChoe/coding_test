a=input()
b=set('CAMBRIDGE')
for i in a:
    if i in set(a)-b:
        print(i,end='')