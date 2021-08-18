def solution(n):
    answer = []
    def hanoi(n,start_point=1, end_point=3, auxiliary_point=2):
        if n==1:
            answer.append([start_point, end_point])
            return
        hanoi(n-1,start_point, auxiliary_point, end_point)
        answer.append([start_point, end_point])
        hanoi(n-1,auxiliary_point, end_point, start_point)
    hanoi(n)
    return answer