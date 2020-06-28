import heapq
def solution(scoville, K):
    cnt=0
    heapq.heapify(scoville)
    while len(scoville)!=1 and scoville[0]<K:
        scoville.append(heapq.heappop(scoville)+heapq.heappop(scoville)*2)
        cnt+=1
    if scoville[0]<K: cnt=-1
    return cnt
print(solution([1, 2, 3, 9, 10, 12], 7))