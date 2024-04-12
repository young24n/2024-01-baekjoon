N, M = map(int, input().split())
cards = list(map(int, input().split()))

close_sum = 0

for i in range(0, N-2):#index 범위 지정, N-2인 이유는 아래에서 이미 해당 index에 접근하기 때문 아래 반복문도 같은 이유
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            sum = cards[i] + cards[j] + cards[k]
            if sum <= M and sum > close_sum: 
                # M보다 작거나 같고 기존값보다 크면 값변경
                close_sum = sum
print(close_sum)