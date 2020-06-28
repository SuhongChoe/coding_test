from collections import deque
def solution(bridge_length, weight, truck_weights):
    length=deque([0]*bridge_length)
    sum=0
    answer=0
    for i in truck_weights:
        while sum+i>weight:
            sum-=length.pop()
            length.appendleft(0)
            if not sum: answer+=1
        length.appendleft(i)
        length.pop()
        sum+=i
        answer+=1
    while length:
        length.pop()
        answer+=1
    return answer
print(solution(2, 10, [7, 4, 5, 6]))