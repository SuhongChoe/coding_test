from collections import deque
def solution(progresses, speeds):
    answer = []
    ll=deque()
    for i in range(len(speeds)):
        n,m=divmod(100-progresses[i],speeds[i])
        if m!=0: n+=1
        ll.append(n)
    while ll:
        cnt=1
        t=ll.popleft()
        for i in range(1,len(ll)):
            if ll[i]>t:
                break
            cnt+=1
            ll.popleft()
        answer.append(cnt)

    return answer

print(solution([95,94,97,95],[1,1,1,1]))