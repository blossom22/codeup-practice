# Codeup_Python 기초100제_6070: 월 입력받아 계절 출력하기
# 12,1,2월은 겨울, 3,4,5월은 봄, 6,7,8월은 여름, 9,10,11월은 가을로 가정한다. 
# 아래처럼 월 숫자의 규칙성으로 해결할 수 있다. 
a = int(input("월을 입력하세요: "))
if a//3 == 1:
    print("spring")
elif a//3 == 2:
    print("summer")
elif a//3 == 3:
    print("fall")
else:
    print("winter")

