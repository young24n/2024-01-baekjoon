T = int(input(""))
# T만큼의 결과값을 담을 results 선언
results = []

for i in range(T):
    #list A 선언과 동시 map으로 input(문자열 상태)을 int형으로 split으로 나누고 저장
    A = list(map(int, input().split()))
    # A를 sorted 정렬 + 내림차순
    sorted_A = sorted(A, reverse=True)
    #정렬된 3번째 값을 results에 저장
    results.append(sorted_A[2])

#결과를 줄바꿈으로 출력
for result in results:
    print(result)