import sys
input = sys.stdin.readline

# 테스트 케이스 수
T = int(input().strip())

for _ in range(T):
    N = int(input().strip())# 후보자 수 입력
    candidates = []
    for _ in range(N):
        d_rank, i_rank = map(int, input().strip().split())# 후보자의 서류 및 면접 점수 입력
        candidates.append((d_rank, i_rank))# 후보자 목록에 추가

    # 서류 점수 기준으로 후보자 정렬
    candidates.sort()

    # 합격자 수 초기화 (첫 번째 후보자는 무조건 합격)
    result = 1
    min_rank = candidates[0][1]# 첫번째 후보자의 면접 점수를 기준 점수로 설정

    for d_rank, i_rank in candidates[1:]:# 첫 번째 후보자는 이미 처리했으므로 제외
        if i_rank < min_rank:# 면접 점수가 현재 기준보다 낮다면(값이 낮은거지 랭크는 높음)
            result += 1# 합격자 추가
            min_rank = i_rank# 새로운 기준 점수로 갱신

    print(result)
