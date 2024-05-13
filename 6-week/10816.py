from collections import Counter
import sys

input = sys.stdin.readline

n = input()#첫번째 줄: 입력할 카드 수(가지고 있는)
card = list(map(int, input().split()))#두번째 줄: 카드에 적힌 정수

m = input()#세번째 줄: 입력할 카드 수(비교할)
sample = list(map(int, input().split()))#네번째 줄: 카드에 적힌 정수

#내장 모듈 Counter -> list 원소를 세어 딕셔너리 형태로 반환   형태 --> 카드번호 : 나온 숫자
count = Counter(card)

#sample 크기 만큼 진행
for i in range(len(sample)):
    if sample[i] in count: # sample 리스트의 i번째 요소가 count 딕셔너리의 키로 존재하는지 확인 
        print(count[sample[i]], end=' ')# count 딕셔너리의 key(sample[i])의 값(카드 등장 수)을 공백으로 구분하여 출력
    else: # 해당 카드가 없으면 0 출력
        print(0, end=' ') 