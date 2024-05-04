n = int(input()) # 로프 입력
k = list() # 각 로프가 버틸 수 있는 무게들

for _ in range(n): 
    k.append(int(input()))
# 굳이 역순 정렬 안해도 될듯?
k.sort()

result = list()

for x in k:
    # 무게 * 로프갯수 -> 해당 로프가 버틸 수 있는 최대 무게
    result.append(x*n)
    n -= 1 # 로프 갯수 줄이기

print(max(result))