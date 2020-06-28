def solution(numbers):
    numbers=sorted(list(map(str,numbers)),reverse=True)
    for i in range(len(numbers)-1):
        j=i
        while j>=0 and int(numbers[j]+numbers[j+1])<int(numbers[j+1]+numbers[j]):
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]
            j-=1
    return ''.join(numbers)
print(solution([12,15]))