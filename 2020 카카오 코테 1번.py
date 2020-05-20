numbers = list(map(int, input().split()))
hand = input()
ans = ""
pad = {1: (1, 1), 2: (2, 1), 3: (3, 1),  # 패드값
       4: (1, 2), 5: (2, 2), 6: (3, 2),
       7: (1, 3), 8: (2, 3), 9: (3, 3),
       0: (2, 4)}
rl = {'left': (1,4), 'right': (3,4)}  # 현재위치
for i in numbers:
    if pad[i][0] == 1:
        rl['left'] = pad[i]
        ans += 'L'
    elif pad[i][0] == 3:
        rl['right'] = pad[i]
        ans += 'R'
    else:
        R = abs(rl['right'][0] - pad[i][0]) + abs(rl['right'][1] - pad[i][1])
        L = abs(rl['left'][0] - pad[i][0]) + abs(rl['left'][1] - pad[i][1])
        if R<L:
            rl['right'] = pad[i]
            ans += 'R'
        elif R>L:
            rl['left'] = pad[i]
            ans += 'L'
        else:
            rl[hand]=pad[i]
            if hand=='right':
                ans+='R'
            else:
                ans+='L'
print(ans)