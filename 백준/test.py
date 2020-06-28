r = int(input())
arr=list(list(range(r))for _ in range(r))

sig = [[1,0],[0,1],[-1,0],[0,-1]]
x= -1
y=0
count =0
for i in range(2*r):
    for _ in range((2*r-i)//2):
        x+=sig[i%4][0]
        y+=sig[i%4][1]
        count+=1
        arr[x][y]=count

for i in range(r):
    for j in range(r):
        print(arr[j][i],end=' ')
    print()