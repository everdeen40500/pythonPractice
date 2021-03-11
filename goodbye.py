#주석 = 코멘트 : 만들다 만 코드를 위해 / 개발자간의 원활한 소통 위해 / 메모를 위해 사용


#파이썬 자료형이 다르면 다른 것이다!
print(2+2.0)
#2와 2.0은 같은 수지만  자료형이 다르므로 다른 것이다. 출력값 또한 4가 아닌 4.0으로 나온다.


#자료형
# 1. 실수
# 2. 정수
# 3. 문자열(string)
# 4. boolean - true/false


#추상화 : 복잡한 기능은 숨기고 중요한 기능만 기억하자!
# 1. 변수 : 값을 저장
# 2. 함수 : 명령들을 저장

# 3. 객체



#변수
#변수 선언법 : 변수이름 = 값(= : 지정연산자)
#변수 사용하는 이유 : 1. 한 번에 수정 용이(수정이 쉽다), 2. 값을 기억 못 해도 코드 작동이 가능하다.
num = 2
print(num)

burger_price = 4990
fries_price = 5990
print(burger_price)
print(burger_price * 2)
print(burger_price * 5 + fries_price * 3)


#함수
#함수 선언법 : def 함수명(parameter): 함수내용
#   ( {} 없이 사용)
def sum(num1, num2): #paramter : 함수에 넘겨주는 값!
    return num1 * num2 #return : 값을 반환!(=돌려준다)

sum(5, 9) #이렇게 하면 콘솔에 출력이 안 된다. -> return은 값을 반환해주지 콘솔에 출력해주진 않는다.
print(sum(5, 9)) #콘솔에 출력 되게 하려면 print()로 감싸야 한다.