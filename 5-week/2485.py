import sys
from math import gcd
# 흠 저번에 크게 의미는 없다고 들은...? 코테용 수법
input = sys.stdin.readline

# 이미 있는 가로수의 갯수 N
N = int(input())

# 첫번째 가로수 위치 
a = int(input())

# 각 가로수의 간격 값을 저장할 배열
arr = []

# 가로수들 사이의 간격 저장
# N-1은 위에서 이미 첫번째 가로수 위치를 입력받아서 빼고 반복 진행
for i in range(N-1):
    # 이후 입력 받는 가로수 위치
    num = int(input())
    # 가로수 간의 간격 저장 
    # (1번에서 2번까지의 간격 2번에서 3번까지의 간격...반복)
    arr.append(num - a)
    # 가로수 위치 업데이트
    a = num

#  최대공약수를 계산하기 위한 시작점
g = arr[0]

# 모든 배열 순회
for j in range(1, len(arr)):
    # 각 간격의 최대공약수를 구하고 해당 값으로 
    # 다시 다음 간격과의 최대공약수를 구함 이렇게 해서 
    # 모든 간격에 대한 최대 공약수가 g에 들어감
    g = gcd(g, arr[j])

# 총 사용 가로수 저장 변수
result = 0

#
for each in arr:
    # 연산자 우선순위 생각하셈
    # === (each // g) - 1
    # 몫을 구하고 -1 --> 각 간격에 모든 간격에 대한 최대공약수 g를 나누어 주면
    # 각 간격에 대한 필요한 가로수 갯수가 나옴 이미 존재하는 가로수가 포함된
    # 값이라 -1을 해줌 result에 그 값을 계속 누적 시킴 -> 필요한 최소 가로수가 구해짐
    result += each // g - 1
print(result)