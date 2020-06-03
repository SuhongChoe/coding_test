def f(n, base):
    sum=0
    while n>0:
        sum+=n%base
        n//=base
    return sum
for i in range(1000, 10000):
    a = f(i, 10)
    b = f(i, 12)
    c = f(i, 16)
    if a == b and b == c:
        print(i)
