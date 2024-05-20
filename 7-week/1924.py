M, D = input().split()
month = int(M)
day = int(D)

# 각 월의 일 수
days_in_month = {
    1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30,
    7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
}

# 각 월의 첫째 날의 요일 (1: 월요일, 2: 화요일, ..., 7: 일요일)
first_day_of_month = {
    1: 1,  # 1월 1일은 월요일
    2: 4,  # 2월 1일은 목요일
    3: 4,  # 3월 1일은 목요일
    4: 7,  # 4월 1일은 일요일
    5: 2,  # 5월 1일은 화요일
    6: 5,  # 6월 1일은 금요일
    7: 7,  # 7월 1일은 일요일
    8: 3,  # 8월 1일은 수요일
    9: 6,  # 9월 1일은 토요일
    10: 1, # 10월 1일은 월요일
    11: 4, # 11월 1일은 목요일
    12: 6  # 12월 1일은 토요일
}

# 요일 매핑 (1: 월요일, 2: 화요일, ..., 7: 일요일)
weekdays = {
    1: 'MON', 2: 'TUE', 3: 'WED', 4: 'THU',
    5: 'FRI', 6: 'SAT', 7: 'SUN'
}

# 주어진 월과 일의 유효성 확인
if month not in days_in_month or day < 1 or day > days_in_month[month]:
    print("Invalid date")
else:
    # 해당 월의 첫째 날의 요일을 가져옴
    first_day = first_day_of_month[month]

    # 해당 일의 요일 계산
    weekday = (first_day + (day - 1)) % 7
    if weekday == 0:
        weekday = 7

    # 결과 출력
    print(weekdays[weekday])
