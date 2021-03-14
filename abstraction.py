# 함수 호출
def square(x):
    return x * x
# 여기까진 그냥 함수를 정의한 것.

# 함수 호출 방법 : 함수명() / 함수명(parameter) => 함수 옆에 ()를 꼭 붙여줘야 한다.
print("함수 호출 전")
print(square(3) + square(4))  #이 부분이 부분이 함수를 호출한 부분.
print("함수 호출 후")


# return문의 역할 :
# (함수가) 무언가를 돌려주는 것. => 함수 호출 부분에 값을 돌려준다.
# 함수를 즉시 종료하기.

def square(x):
    print("함수 시작!")
    return x * x  #square함수는 여기까지만 실행 후 종료된다.
    print("함수 종료!")  #따라서 이 부분은 dead code(의미 없는 코드)이다. => 실행 되지 X

print(square(3))
print("hello world!!")




# return과 print의 차이
def print_square(x):
    print(x * x)

def get_square(x):
    return (x * x)

get_square(3)  #9값을 돌려주기만 했지 콘솔에 출력되진 않는다.
print(get_square(3))  #print()로 씌워줬기 때문에 9값이 출력된다.
print("---- print(print_square(3))의 값은?? -----")
print(print_square(3))  #파이썬에선 return 값이 없으면 없다는 의미로 None이 return된다.
# 따라서 print(print_square(3))에서 print_square(3)은 9가 출력이 되고 return 값이 없으니 None이 return 되어
# print(None)이 된다. None값도 print()에 의해 출력이 되서 총 콘솔 출력값은 9 None이 된다!!



# optional parameter
# parameter 값을 미리 지정해주는 것.
# 해당 parameter에 값을 지정 안 하고 함수 호출할 경우, 미리 지정해놓은 파라미터 값이 출력된다.
def myself(name, age, nationality="한국"):
    print("내 이름은 {}".format(name))
    print("나이는 {}살".format(age))
    print("국적은 {}".format(nationality))


print()
print("==== optional parameter =====")
myself("taylor", 1, "미국")  # 옵셔널 파라미터를 제공하는 경우
print()
myself("taylor", 1)



# syntactic sugar
# 다음 두 줄은 같습니다
x = 4
x = x + 1
x += 1

# 다음 두 줄은 같습니다
x = x + 2
x += 2

# 다음 두 줄은 같습니다
x = x * 2
x *= 2

# 다음 두 줄은 같습니다
x = x - 3
x -= 3

# 다음 두 줄은 같습니다
x = x / 2
x /= 2

# 다음 두 줄은 같습니다
x = x % 7
x %= 7




# scope : 변수 사용 가능 범
# global scope : global 변수는 모든 곳에서 사용 가능.
# local scope : 변수 정의한 함수 내에서만 사용 가능. (parameter도 local 변수다!)
# 함수에서 변수 사용시 먼저 함수 내에서 정의된 local 변수를 찾고 없으면 global scope에서 찾기.
print()
x = 2  #global 변수 x

def my_function():
    x = 3  #local 변수
    print(x)

my_function()  #my_function 함수 실행
print(x)  #global 변수 x가 사용 된다.




# 상수 : "값이 변하지 않음" (constant)
# - 대문자로 써야 함.
# 1. 일반 변수와 상수를 쉽게 구분짓기 위함.
# 2. 실수로 상수 변경하지 않기 위함!
PI = 3.14

def calculate_area(r):
    return PI * r * r

radius = 4
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

PI = 0  #상수를 변경해 작동할 수 있지만 이건 잘못된 코드다. 애초에 상수로 설정한 이유가 값이 일정하도록(변하지 X) 하기 위함이니까!
radius = 6
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))

radius = 7
print("반지름이 {}면, 넓이는 {}".format(radius, calculate_area(radius)))




# 스타일 : "이해하기 쉬운 코드(가독성 좋은)가 스타일이 좋은 코드다!"
# 변수 이름을 그 뜻을 잘 살려 지정해야 한다.
# 스페이스, 엔터키(화이트 스페이스)를 잘 사용해야 한다.
# 일정한 명령어들은 함수로 만들어서 사용.

# 파이썬 스타일 가이드 : PEP8



