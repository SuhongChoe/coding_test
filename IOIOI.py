p='OI'
n=int(input())
p='I'+p*n
input()
s=input()
cnt=0
ans=0
u=False
for i in range(len(s)):
    if p:
        p=False
        continue
    if s[i]=='I':
        u=True
        cnt=0
        continue
    if u:
        if s[i:i+2] =='OI':
            cnt+=1
            p=True
            if n==cnt:
                ans+=1
                cnt-=1
        else:
            u=False
            cnt=0
print(ans)