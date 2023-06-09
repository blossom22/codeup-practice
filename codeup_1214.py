# Codeup_Python 기초3.if~else_1214: 이 달은 며칠까지 있을까?

a, b = map(int, input("연도와 월을 입력하세요: ").split())

days = 31       # 어차피 얻고자 하는 값은 '일수'이므로 얘를 먼저 지정해주고 시작하자. 
if b == 2:      # 2월조건
    if (a % 400 == 0) or (a % 4 == 0 and a % 100 != 0):     # 윤년조건
        days = 29                                           # 윤년일때 2월은 29일
    else:                                                   # 윤년아닐때 2월은 28일
        days = 28
elif b in [4, 6, 9, 11]:    # 30일로 끝나는 '월'
    days = 30

print(days)                 # 1,3,5,7,8,10,12월 입력시, 초기설정한 days값인 31일로 출력된다. 