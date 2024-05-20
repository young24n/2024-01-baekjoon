import sys

input = sys.stdin.readline

N = int(input())
points = list()

for _ in range(N):
    x, y = map(int, input().split())
    points.append((x, y))

# points를 x좌표, y좌표 순으로 정렬
points.sort(key=lambda point: (point[0], point[1]))

# 정렬된 좌표 출력
for point in points:
    print(point[0], point[1])