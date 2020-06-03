ll = input().strip()
temp = []
for i in ll:
    if i == '+' or i == '-':
        while temp and temp[len(temp) - 1] != '(':
            print(temp.pop(), end='')
        temp.append(i)
    elif i == '*' or i == '/':
        while temp and temp[len(temp) - 1] != '(' and temp[len(temp) - 1] != '+' and temp[len(temp) - 1] != '-':
            print(temp.pop(), end='')
        temp.append(i)
    elif i == '(':
        temp.append(i)
    elif i == ')':
        while temp and temp[len(temp) - 1] != '(':
            print(temp.pop(), end='')
        temp.pop()
    else:
        print(i, end='')
while temp:
    print(temp.pop(), end='')
