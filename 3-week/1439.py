from itertools import groupby

#문자열입력
str = input()
#초기화
countZero = 0
countOne = 0

#key는 연속된 구간의 문자를 반환 
#group은 분리된 문자 전체를 LIST형태로 반환한다 
#사용하지는 않지만 key를 반환받기 위해 두가지를 지정
for key, group in groupby(str):
    if key == '0':
        countZero += 1
    elif key == '1':
        countOne += 1

#연속된 구간이 가장 적은 값 탐색
# 11111 같이 들어와도 초기화된 0이 선택됨
val = min(countZero, countOne)

print(val)