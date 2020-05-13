import sys;input = sys.stdin.readline
students = [tuple(input().split()) for _ in range(int(input()))]
for i in sorted(students, key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0])):
    print(i[0])
