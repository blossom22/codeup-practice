# Codeup_Python 기초3.if~else_1229: 비만도 측정 2

a,b=map(float, input("키와 몸무게를 입력하세요: ").split())
c=0
(c:=a-100) if a<150 else (c:=(a-100)*0.9) if a>=160 else (c:=(a-150)/2+50)
d=(b-c)*100/c
print("정상") if d<=10 else print("비만") if d>20 else print("과체중")

# 5번째줄에서 바다코끼리 연산자를 사용했다. (:=)
# 할당과 반환을 동시에 하는 것으로    변수:=표현식    꼴로 쓰이는데, 표현식의 결과를 변수에 할당하고 동시에 반환까지 하는 것이다. 
# 위에서 만약 내가 :=을 쓰지 않았다면, 변수c에 들어갈 표현식을 작성하기 위해 코드를 더 길게 썼어야 할 것이다. 