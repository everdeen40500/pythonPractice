# 정수 연산 정수 = 정수
# 정수 연산 실수 = 실수
# 실수 연산 실수 = 실수



# n 제곱승 : **s
print( 2 ** 3)

# / - 나누기 , % - 나누기 나머지 몫

# /는 무조건 결과 실수
print( 7/ 2)

#floor division (버림 나눗셈) : 나눴을 때 몫의 소수부분이 사라진다.
print(7 // 2)
print(3.0 // 2) #둘 중 하나가 소수형이면 값도 소수형(소수점 아래는 0으로 -> 6.0)

#round (반올림)
print("---- round ----")
print(round(3.1481592, 2)) #소수점 2째자리에서 반올림
print(round(3.141592)) #소수점 밑으로 다 삭제, 소수점 앞 부분만(정수 부분)

# 문자열
# 문자열에 싱글/더블 따옴표 여러개 있을 때 해당 따옴표 앞에 \(역슬러쉬)를 붙여준다.
print("I\'m \"excited to learn python!")


# 0314
# 형 변환(type conversion = type casting)
# 형 변환 방법 : 원하는자료형(변환시키고싶은것)
print(int(3.8))
print(float(3))
print(int("2") + int("5"))
print(float("1.1") + float("2.5"))
print(str(2) + str(5))

age = 7
# str(age) 없이 그냥 age만 넣을 경우 오류가 난다. => 자료형이 일치하지 않기 때문에!!
# => 그래서 형변환을 시켜줘서 자료형을 일치 시켜줘야 한다.
print("제 나이는 " + str(age) + "입니다.")

# 형 변환할 때 논리적으로 말이 되는지 확인해야 한다!
# print(int("hello world!")) -> 오류가 난다.


# ex. 오늘은 2019년 10월 29일입니다.
year = 2019
month = 10
day = 29

print("오늘은 " + str(year) + "년 " + str(month) + "월 " + str(day) + "일입니다.")
# format 메소드
# 사용방법 : {}, 메소드 파라미터에 차례대로 중괄호에 넣고 싶은 변수를 써준다.
print("오늘은 {}년 {}월 {}일입니다.".format(year, month, day))

date_string = "오늘은 {}년 {}월 {}일입니다."
print(date_string.format(year, month, day))

# format 메소드 출력되는 순
print("저는 {1}, {0}, {2}를 좋아합니다.".format("taylor swift", "yunakim", "beyonce"))

num_1 = 1
num_2 = 3
print("{0} 나누기 {1}은 {2}입니다.".format(num_1, num_2, num_1 / num_2))
# :.nf  => f는 floating point의 약자, .n은 소수점 n째 자리에 반올림하란
print("{0} 나누기 {1}은 {2:.2f}입니다.".format(num_1, num_2, num_1 / num_2))
# :.0f => 소수점 0째 자리에 반올림 하란 뜻이니까 정수자리만 출력하란 뜻!
print("{0} 나누기 {1}은 {2:.0f}입니다.".format(num_1, num_2, num_1 / num_2))



# 불 대수 : 일상적인 논리를 수학적으로 표현한 것.  == 논리 연산
# 명제(참과 거짓이 확실한 문장)가 있어야 한다.
# 불 대수 값(진리값) : true, false
# and, or, not
# and : 둘 다 참일 때 true이다.
# or : 둘 중 하나라도 참이면 true다.
# not : 반대로 뒤집어준다.


# 불린 (Boolean)
# True / False : 앞글자 무조건 대문자로!!
print(True)
print(False)

# not, and, or 연산자는 다 영어 소문자로!! ( & | ! 이런 거 없나봄..)
print(True and True)
print(False or True)
print(not True)

# f or t => not true => false or false -> false
x = 3
print(x > 4 or not (x < 2 or x == 3))



# type 함수 : 어떤 자료형인지 알려준다.
print(type(3))
print(type(3.0)) #floating point(실수)의 줄임말인 float가 자료형으로 출력된다.
print(type("hello"))
print(type(True))
print(type("False"))

def hello():
    print("hi taylor!!")

print(type(hello))
print(type(print)) #builtin => 내장된 함수란 뜻