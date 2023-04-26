# Codeup_Python 기초100제_6026: 실수 2개 입력받아 합 계산하기
a = float(input("첫번째 수를 입력하세요: "))
b = float(input("두번째 수를 입력하세요: "))
print(a+b)

# 그러나 여기서 a를 0.1, b는 0.2로 하면 0.3이 나오지 않는다. 0.3000...0004로 이상하게 나온다. 
# 알아본 결과, 우리가 입력한 0.1과 0.2는 실제 0.1, 0.2가 아니다. 
# 이유는 컴퓨터가 이진법으로 데이터를 처리하기 때문이다. 이진법에서는 1/10이 무한소수가 된다. 
# 마치 십진법에서는 1/3이 0.33333.....이런 무한소수가 되듯이 말이다. 
# 그래서 특정 자릿수에서 반올림을 해서 더하니까, 실제값보다 살짝 큰 0.30000...004 같은 소수가 나오는 것이다. 

# 컴퓨터는 메모리를 가장 효율적으로 활용할 수 있는 방식으로 데이터를 저장한다.
# 우리가 쓰는 주요 숫자 자료형은 int와 float가 있다. 
# int는 소수점없는 정수 데이터를 저장하는 자료형이다. 이것은 32비트를 사용하는데, 
# 첫번째 자리가 부호를 의미(0은 양수, 1은 음수), 나머지 31자리으로 절대값을 표현한다.
# 이렇게 32비트(4바이트)로 정수 표현하는 것이 int자료형이다. 이 바이트 수를 다르게 해서 여러 정수 자료형을 가진다.

# 부동소수점(floating point)자료형을 보자.(말그대로 소수점이 움직인다는 의미)
# 만약 int자료형처럼 31비트내에서 정수부분과 소수부분을 딱 나누어서 쓰면 (고정소수점 방식)
# 정수부분은 큰 수를 표현할 수 없고, 소수부분도 정확한 값을 표현할 수 없다.
# 정수부분에 비트를 더 할당하면 나타내는 소수점자리가 제한되고, 반대로 소수부분을 늘리면 가용한 절대값크기가 줄어든다.
# 그래서 이것대신 부동소수점 방식을 쓴다. (모든 이진수숫자를 1.xxxx...의 형식으로 바꾼다=즉, 소수점자리를 옮긴다)
# 32비트중 첫번째자리는 부호를 나타내고, 그다음의 8비트로 소수점이 몇 칸움직일지 나타낸다. (소수점자리 옮긴 만큼의 숫자+127을 2진수로 표현)
# 나머지 23자리에 소수점이 움직인 결과에서 소숫점 뒤로 오는 부분을 채운다. 
# 이방식을 쓰면 23비트를 숫자 표현에 쓰고, 소숫점 자리도 필요한대로 움직여서 고정소수점보다는 더 효율적으로 비트 활용이 가능하다.
# 한정된 메모리를 최대한 활용하다보니 이런 부동소수점 같은것이 생긴것이다. 

# 위에서 배울 수 있는 것: 정확한 계산해야는 상황이면, float을 쓰면 안되고 정수형 자료를 써야한다. 만약 float을 반드시 써야한다면, 반올림문법을 쓰거나,
# double 자료형을 쓰면된다.(double을 쓰면, 32비트가 아닌 64비트로 써서 오차가 매우 작아진다. 단, 메모리 용량을 2배 잡아먹음)